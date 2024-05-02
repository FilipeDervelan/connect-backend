from app.models import Ministry
from application.useCases.ListMinistries.protocols.ListMinistriesRequest import ListMinistriesRequest
from application.useCases.ListMinistries.protocols.ListMinistriesResponse import ListMinistriesResponse


class ListMinistries:
    def execute(self, inbound: ListMinistriesRequest) -> ListMinistriesResponse:
        ministriesList = []
        ministries = Ministry.objects.all()

        for item in ministries:
            ministriesList.append({
                "id": item.id,
                "name": item.name,
                "description": item.description
            })

        result = ListMinistriesResponse()
        result.response = ministriesList
        result.status = 200

        return result