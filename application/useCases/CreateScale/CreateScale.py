from datetime import datetime
from django.db.models import Q
from app.models import Ministry, Scale, Unavailability, User
from application.useCases.CreateScale.protocols.CreateScaleRequest import CreateScaleRequest
from application.useCases.CreateScale.protocols.CreateScaleResponse import CreateScaleResponse

class CreateScale:
    def execute(self, inbound: CreateScaleRequest) -> CreateScaleResponse:
        name = inbound.name
        description = inbound.description
        date = inbound.date
        songs = inbound.song
        participants = inbound.participants
        functions = inbound.function
        ministryId = inbound.ministry_id

        result = CreateScaleResponse()

        if not name:
            result.response = "Name is required"
            result.status = 400
            return result

        if not date:
            result.response = "Date is required"
            result.status = 400
            return result

        if not ministryId:
            result.response = "A ministry is required"
            result.status = 400
            return result

        dateFormatted = datetime.strptime(date, '%d/%m/%Y')
        dateFormatted = dateFormatted.strftime('%Y-%m-%d')
        
        ministry = Ministry.objects.get(id=ministryId)

        exists = Scale.objects.filter(date=dateFormatted, ministry=ministry.id).first()

        if exists:
            result.response = "A scale alreay exists for this day and this ministry"
            result.status =  400

            return result

        newScale = Scale(name=name, description=description, date=dateFormatted, ministry=ministry)

        newScale.save()

        scale = Scale.objects.get(date=dateFormatted, name=name)

        participantsWithUnavailabilities = []

        for id in participants:
            userRecovered = User.objects.get(id=id)

            unavailability = Unavailability.objects.filter(
                Q(user=userRecovered.id) &
                Q(start_date__lte=dateFormatted) & Q(end_date__gte=dateFormatted) |
                Q(start_date=dateFormatted) |
                Q(end_date=dateFormatted)
            ).first()

            if unavailability:
                message = f"{userRecovered.name} ({unavailability.start_date} - {unavailability.end_date})"

                participantsWithUnavailabilities.append(message)

            scale.participant.add(userRecovered)
        
        if len(participantsWithUnavailabilities) > 0:
            result.response = f"Some participants are not available for the scale: {participantsWithUnavailabilities}"
        else:
            result.response = "Scale successfully created"
            
        result.status = 201

        return result
