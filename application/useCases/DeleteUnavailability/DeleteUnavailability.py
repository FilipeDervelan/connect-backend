from app.models import Unavailability
from application.useCases.DeleteUnavailability.protocols.DeleteUnavailabilityRequest import (
    DeleteUnavailabilityRequest,
)
from application.useCases.DeleteUnavailability.protocols.DeleteUnavailabilityResponse import (
    DeleteUnavailabilityResponse,
)


class DeleteUnavailability:
    def execute(
        self,
        inbound: DeleteUnavailabilityRequest,
    ) -> DeleteUnavailabilityResponse:
        outbound = DeleteUnavailabilityResponse()
        outbound.response = "Unavailability deleted"
        outbound.status = 200

        obj = Unavailability.objects.get(id=inbound.id)

        obj.delete()

        return outbound
