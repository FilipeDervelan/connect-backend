from app.models import Scale
from application.useCases.GetScale.protocols.GetScaleRequest import GetScaleRequest
from application.useCases.GetScale.protocols.GetScaleResponse import GetScaleResponse


class GetScale:
    def execute(self, inbound: GetScaleRequest) -> GetScaleResponse:
        outbound = GetScaleResponse()

        scale = Scale.objects.get(id=inbound.id)

        scale_dict = {
            "id": scale.id,
            "name": scale.name,
            "description": scale.description,
            "date": scale.date,
            "ministry": {
                "id": scale.ministry.id,
                "name": scale.ministry.name,
            },
            "songs": [
                {
                    "id": song.id,
                    "name": song.name,
                }
                for song in scale.song.all()
            ],
            "participants": [
                {
                    "id": participant.id,
                    "name": participant.username,
                }
                for participant in scale.participant.all()
            ],
            "created_by": scale.created_by,
            "created_at": scale.created_at,
            "updated_at": scale.updated_at,
        }

        outbound.result = scale_dict

        return outbound
