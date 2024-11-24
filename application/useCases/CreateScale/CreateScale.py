from datetime import datetime
from django.db.models import Q
from app.models import CustomUser, Ministry, Scale, Song, Unavailability
from application.useCases.CreateScale.protocols.CreateScaleRequest import (
    CreateScaleRequest,
)
from application.useCases.CreateScale.protocols.CreateScaleResponse import (
    CreateScaleResponse,
)


class CreateScale:
    def execute(self, inbound: CreateScaleRequest) -> CreateScaleResponse:
        name = inbound.name
        description = inbound.description
        date = inbound.date
        songs = inbound.song
        participants = inbound.participants
        ministry_id = inbound.ministry_id

        result = CreateScaleResponse()

        if not name:
            result.response = "Name is required"
            result.status = 400
            return result

        if not date:
            result.response = "Date is required"
            result.status = 400
            return result

        if not ministry_id:
            result.response = "A ministry is required"
            result.status = 400
            return result

        formatted_date = datetime.strptime(date, "%d/%m/%Y")
        formatted_date = formatted_date.strftime("%Y-%m-%d")

        ministry = Ministry.objects.get(id=ministry_id)

        scale = Scale.objects.filter(
            date=formatted_date,
            ministry=ministry.id,
        ).first()

        if scale:
            result.response = "A scale already exists for this day and this ministry"
            result.status = 400

            return result

        new_scale = Scale(
            name=name,
            description=description,
            date=formatted_date,
            ministry=ministry,
        )

        new_scale.save()

        scale = Scale.objects.get(date=formatted_date, name=name)

        participants_with_unavailabilities = []

        for song_id in songs:
            song = Song.objects.get(id=song_id)

            if song in scale.song:
                continue

            scale.song.add(song)

        for id in participants:
            user = CustomUser.objects.get(id=id)

            unavailability = Unavailability.objects.filter(
                Q(user=user.id)
                & Q(start_date__lte=formatted_date)
                & Q(end_date__gte=formatted_date)
                | Q(start_date=formatted_date)
                | Q(end_date=formatted_date)
            ).first()

            if unavailability:
                message = f"{user.username} ({unavailability.start_date} - {unavailability.end_date})"

                participants_with_unavailabilities.append(message)

            scale.participant.add(user)

        if len(participants_with_unavailabilities) > 0:
            result.response = f"Some participants are not available for the scale: {participants_with_unavailabilities}"
        else:
            result.response = "Scale successfully created"

        result.status = 201

        return result
