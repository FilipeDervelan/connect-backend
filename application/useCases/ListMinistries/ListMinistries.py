from app.models import CustomUser, Ministry, Scale

from application.useCases.ListMinistries.protocols.ListMinistriesResponse import (
    ListMinistriesResponse,
)


class ListMinistries:
    def execute(self) -> ListMinistriesResponse:
        ministries_list = []
        ministries = Ministry.objects.all()

        for item in ministries:
            scales_list = []
            scales = Scale.objects.filter(ministry=item.id)
            participants = CustomUser.objects.filter(ministry=item.id)

            for scale in scales:
                scales_list.append(
                    {
                        "id": scale.id,
                        "name": scale.name,
                        "description": scale.description,
                        "date": scale.date,
                        "songs": [song.id for song in scale.song.all()],
                        "participants": [
                            participant.id for participant in scale.participant.all()
                        ],
                        "ministry_id": scale.ministry.id,
                    }
                )

            ministries_list.append(
                {
                    "id": item.id,
                    "name": item.name,
                    "description": item.description,
                    "scales": scales_list,
                    "participants": [
                        {
                            "id": participant.id,
                            "name": participant.username,
                            "birth_day": participant.birth_day,
                        }
                        for participant in participants
                    ],
                }
            )

        result = ListMinistriesResponse()
        result.response = ministries_list

        return result
