from app.models import Ministry, Scale
from application.useCases.ListMinistries.protocols.ListMinistriesRequest import ListMinistriesRequest
from application.useCases.ListMinistries.protocols.ListMinistriesResponse import ListMinistriesResponse


class ListMinistries:
    def execute(self, inbound: ListMinistriesRequest) -> ListMinistriesResponse:
        ministriesList = []
        ministries = Ministry.objects.all()

        scaleList = []

        for item in ministries:
            scales = Scale.objects.filter(id=item.id)

            for scale in scales:
                scaleList.append({
                    "id": scale.id,
                    "name": scale.name,
                    "description": scale.description,
                    "date": scale.date,
                    "songs": scale.song,
                    "participants": scale.participant,
                    "functions": scale.function
                })

            ministriesList.append({
                "id": item.id,
                "name": item.name,
                "description": item.description,
                "scales": scaleList
            })

        result = ListMinistriesResponse()
        result.response = ministriesList

        return result