from datetime import datetime
from app.models import CustomUser, Unavailability
from application.useCases.CreateUnavailability.protocols.CreateUnavailabilityRequest import (
    CreateUnavailabilityRequest,
)
from application.useCases.CreateUnavailability.protocols.CreateUnavailabilityResponse import (
    CreateUnavailabilityResponse,
)


class CreateUnavailability:
    def execute(
        self,
        inbound: CreateUnavailabilityRequest,
    ) -> CreateUnavailabilityResponse:
        user = CustomUser.objects.get(id=inbound.user_id)

        start_date = datetime.strptime(inbound.start_date, "%d/%m/%Y")
        start_date = start_date.strftime("%Y-%m-%d")

        end_date = datetime.strptime(inbound.end_date, "%d/%m/%Y")
        end_date = end_date.strftime("%Y-%m-%d")

        newUnavailability = Unavailability(
            start_date=start_date,
            end_date=end_date,
            user=user,
        )

        newUnavailability.save()

        result = CreateUnavailabilityResponse()
        result.response = "Successfully created"
        result.status = 201

        return result
