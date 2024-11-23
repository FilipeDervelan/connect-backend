from app.models import Ministry
from application.useCases.DeleteMinistry.protocols.DeleteMinistryRequest import (
    DeleteMinistryRequest,
)
from application.useCases.DeleteMinistry.protocols.DeleteMinistryResponse import (
    DeleteMinistryResponse,
)


class DeleteMinistry:
    def execute(
        self,
        inbound: DeleteMinistryRequest,
    ) -> DeleteMinistryResponse:
        obj = Ministry.objects.get(id=inbound.id)

        obj.delete()

        result = DeleteMinistryResponse()
        result.response = "Ministry successfully deleted"
        result.status = 200

        return result
