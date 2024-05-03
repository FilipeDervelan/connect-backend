from datetime import datetime
from app.models import Ministry, Scale, Song, User
from application.useCases.UpdateScale.protocols.UpdateScaleRequest import UpdateScaleRequest
from application.useCases.UpdateScale.protocols.UpdateScaleResponse import UpdateScaleResponse


class UpdateScale:
    def execute(self, inbound: UpdateScaleRequest) -> UpdateScaleResponse:
        obj = Scale.objects.get(id=inbound.id)

        date = datetime.strptime(inbound.date, '%d/%m/%Y')
        date = date.strftime('%Y-%m-%d')

        obj.name = inbound.name
        obj.description = inbound.description
        obj.date = inbound.date

        for song in inbound.songs:
            scaleSong = Song.objects.get(id=song)

            obj.song.add(scaleSong)

        for participant in inbound.participants:
            scaleParticipant = User.objects.get(id=participant)

            obj.participant.add(scaleParticipant)

        ministry = Ministry.objects.get(id=inbound.ministry_id)

        obj.ministry = ministry
        obj.updated_at = datetime.now()

        obj.save()

        result = UpdateScaleResponse()
        result.response = "Scale updated"
        result.status = 200

        return result