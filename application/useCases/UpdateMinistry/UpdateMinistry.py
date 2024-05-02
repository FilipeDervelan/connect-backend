from datetime import datetime
from app.models import Ministry
from application.useCases.UpdateMinistry.protocols.UpdateMinistryRequest import UpdateMinistryRequest
from application.useCases.UpdateMinistry.protocols.UpdateMinistryResponse import UpdateMinistryResponse


class UpdateMinistry:
    def execute(self, inbound: UpdateMinistryRequest) -> UpdateMinistryResponse:
        obj = Ministry.objects.get(id=inbound.id)

        obj.name = inbound.name
        obj.description = inbound.description or None
        obj.updated_at = datetime.now()

        obj.save()

        result = UpdateMinistryResponse()
        result.response = "Ministry successfully updated"
        result.status = 200

        return result