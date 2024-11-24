from app.models import Scale

from application.useCases.ListScales.protocols.ListScalesResponse import (
    ListScalesResponse,
)


class ListScales:
    def execute(self) -> ListScalesResponse:
        scales_list = []
        scales = Scale.objects.all()

        result = ListScalesResponse()

        for item in scales:
            scales_list.append(
                {
                    "id": item.id,
                    "name": item.name,
                    "description": item.description,
                    "date": item.date,
                    "songs": [
                        {"id": song.id, "name": song.name} for song in item.song.all()
                    ],
                    "participants": [
                        {"id": participant.id, "name": participant.username}
                        for participant in item.participant.all()
                    ],
                    "ministry": {"id": item.ministry.id, "name": item.ministry.name},
                }
            )

        result.response = scales_list
        result.status = 200

        return result
