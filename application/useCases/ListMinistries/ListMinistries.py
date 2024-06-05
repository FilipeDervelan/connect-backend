from app.models import Ministry, Scale, User
from application.useCases.ListMinistries.protocols.ListMinistriesRequest import ListMinistriesRequest
from application.useCases.ListMinistries.protocols.ListMinistriesResponse import ListMinistriesResponse


class ListMinistries:
    def execute(self, inbound: ListMinistriesRequest) -> ListMinistriesResponse:
        ministriesList = []
        ministries = Ministry.objects.all()

        for item in ministries:
            scaleList = []
            scales = Scale.objects.filter(ministry=item.id)
            participants = User.objects.filter(ministry=item.id)

            for scale in scales:
                scaleList.append({
                    "id": scale.id,
                    "name": scale.name,
                    "description": scale.description,
                    "date": scale.date,
                    "songs": [song.id for song in scale.song.all()],
                    "participants": [participant.id for participant in scale.participant.all()],
                    "functions": [function.id for function in scale.function.all()],
                    "ministry_id": scale.ministry.id
                })

            ministriesList.append({
                "id": item.id,
                "name": item.name,
                "description": item.description,
                "scales": scaleList,
                "participants": [{
                    "id": participant.id,
                    "name": participant.name,
                    "birth_day": participant.birth_day
                } for participant in participants]
            })

        result = ListMinistriesResponse()
        result.response = ministriesList

        return result