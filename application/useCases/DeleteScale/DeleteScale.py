from app.models import Scale
from application.useCases.DeleteScale.protocols.DeleteScaleRequest import DeleteScaleRequest
from application.useCases.DeleteScale.protocols.DeleteScaleResponse import DeleteScaleResponse


class DeleteScale:
    def execute(self, inbound: DeleteScaleRequest) -> DeleteScaleResponse:
        scale = Scale.objects.get(id=inbound.id)

        scale.delete()

        result = DeleteScaleResponse()
        result.response = "Scale deleted"
        result.status = 200

        return result