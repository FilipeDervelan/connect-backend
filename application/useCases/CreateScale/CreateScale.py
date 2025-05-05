from datetime import datetime
from django.db import IntegrityError
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from app.models import CustomUser, Ministry, Scale, Song, Unavailability
from application.useCases.CreateScale.protocols.CreateScaleRequest import (
    CreateScaleRequest,
)
from application.useCases.CreateScale.protocols.CreateScaleResponse import (
    CreateScaleResponse,
)


class CreateScale:
    def execute(self, inbound: CreateScaleRequest) -> CreateScaleResponse:
        result = CreateScaleResponse()

        try:
            formatted_date = datetime.strptime(
                inbound.date,
                "%d/%m/%Y",
            ).strftime("%Y-%m-%d")

        except ValueError:
            raise ValueError("Invalid date format. Use DD/MM/YYYY.")

        ministry = Ministry.objects.get(id=inbound.ministry_id)

        scale, created = Scale.objects.get_or_create(
            date=formatted_date,
            ministry=ministry,
            defaults={
                "name": inbound.name,
                "description": inbound.description,
            },
        )

        if not created:
            raise IntegrityError(
                "A scale already exists for this day and this ministry."
            )

        songs = Song.objects.filter(id__in=inbound.song)
        scale.song.add(*songs)

        participants_with_unavailabilities = []
        users = CustomUser.objects.filter(id__in=inbound.participants)

        for user in users:
            unavailability = Unavailability.objects.filter(
                Q(user=user)
                & (
                    Q(
                        start_date__lte=formatted_date,
                        end_date__gte=formatted_date,
                    )
                    | Q(start_date=formatted_date)
                    | Q(end_date=formatted_date)
                )
            ).first()

            if unavailability:
                participants_with_unavailabilities.append(
                    f"{user.username} ({unavailability.start_date} - {unavailability.end_date})"
                )
            else:
                scale.participant.add(user)

        if participants_with_unavailabilities:
            result.response = (
                "Some participants are not available for the scale: "
                + ", ".join(participants_with_unavailabilities)
            )
        else:
            result.response = "Scale successfully created."

        return result
