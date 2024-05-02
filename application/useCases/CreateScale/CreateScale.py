from datetime import datetime
from app.models import Ministry, Scale, User
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

        userList = []

            
        ministry = Ministry.objects.get(id=ministryId)

        newScale = Scale(name=name, description=description, date=dateFormatted, ministry=ministry)

        newScale.save()

        scale = Scale.objects.get(date=dateFormatted)

        for id in participants:
            userRecovered = User.objects.get(id=id)
            scale.participant.add(userRecovered)
            
        result.response = "Scale successfully created"
        result.status = 201

        return result
