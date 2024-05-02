from app.models import Unavailability
from application.useCases.ListUnavailabilities.protocols.ListUnavailabilitiesRequest import ListUnavailabilitiesRequest
from application.useCases.ListUnavailabilities.protocols.ListUnavailabilitiesResponse import ListUnavailabilitiesResponse


class ListUnavailabilities:
    def execute(self, inbound: ListUnavailabilitiesRequest) -> ListUnavailabilitiesResponse:
        unavailabilitiesList = []

        unavailabilities = Unavailability.objects.all()

        for item in unavailabilities:
            unavailabilitiesList.append({
                "id": item.id,
                "user_name": item.user.name,
                "start_date": item.start_date,
                "end_date": item.end_date
            })

        result = ListUnavailabilitiesResponse()
        result.response = unavailabilitiesList
        result.status = 200

        return result