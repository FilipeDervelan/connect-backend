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
                    "songs": item.song.name,
                    "participants": item.participant.name,
                    "functions": item.function.name,
                    "ministry": item.ministry.name,
                }
            )

        result.response = scales_list
        result.status = 200

        return result
