from app.models import CustomUser, Ministry
from application.useCases.DeassignMinistry.protocols.DeassignMinistryRequest import (
    DeassignMinistryRequest,
)
from application.useCases.DeassignMinistry.protocols.DeassignMinistryResponse import (
    DeassignMinistryResponse,
)


class DeassignMinistry:
    def execute(
        self,
        inbound: DeassignMinistryRequest,
    ) -> DeassignMinistryResponse:
        user = CustomUser.objects.get(id=inbound.user_id)
        ministry = Ministry.objects.get(id=inbound.ministry_id)

        result = DeassignMinistryResponse()

        user.ministry.remove(ministry)

        result.response = "Ministry deassigned"
        result.status = 200

        return result
