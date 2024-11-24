from datetime import datetime
from app.models import CustomUser, Ministry, Scale, Song
from application.useCases.UpdateScale.protocols.UpdateScaleRequest import (
    UpdateScaleRequest,
)
from application.useCases.UpdateScale.protocols.UpdateScaleResponse import (
    UpdateScaleResponse,
)


class UpdateScale:
    def execute(self, inbound: UpdateScaleRequest) -> UpdateScaleResponse:
        obj = Scale.objects.get(id=inbound.id)

        date = datetime.strptime(inbound.date, "%d/%m/%Y")
        date = date.strftime("%Y-%m-%d")

        obj.name = inbound.name
        obj.description = inbound.description
        obj.date = date

        song_objects = Song.objects.filter(id__in=inbound.songs)
        obj.song.set(song_objects)

        participant_objects = CustomUser.objects.filter(
            id__in=inbound.participants,
        )
        obj.participant.set(participant_objects)

        obj.updated_at = datetime.now()
        obj.save()

        result = UpdateScaleResponse()
        result.response = "Scale updated"
        result.status = 200

        return result
