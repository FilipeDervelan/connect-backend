from app.models import Unavailability

from application.useCases.ListUnavailabilities.protocols.ListUnavailabilitiesResponse import (
    ListUnavailabilitiesResponse,
)


class ListUnavailabilities:
    def execute(self) -> ListUnavailabilitiesResponse:
        unavailabilities_list = []

        unavailabilities = Unavailability.objects.all()

        for item in unavailabilities:
            unavailabilities_list.append(
                {
                    "id": item.id,
                    "user_name": item.user.name,
                    "start_date": item.start_date,
                    "end_date": item.end_date,
                }
            )

        result = ListUnavailabilitiesResponse()
        result.response = unavailabilities_list
        result.status = 200

        return result
