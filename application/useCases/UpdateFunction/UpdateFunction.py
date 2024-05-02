from app.models import Function, Ministry
from application.useCases.UpdateFunction.protocols.UpdateFunctionRequest import UpdateFunctionRequest
from application.useCases.UpdateFunction.protocols.UpdateFunctionResponse import UpdateFunctionResponse


class UpdateFunction:
    def execute(self, inbound: UpdateFunctionRequest) -> UpdateFunctionResponse:
        ministry = Ministry.objects.get(id=inbound.ministry_id)

        obj = Function.objects.get(id=inbound.id)

        obj.name = inbound.name
        obj.description = inbound.description
        obj.ministry = ministry

        obj.save()

        result = UpdateFunctionResponse()
        result.response = "Function successfully updated"
        result.status = 200

        return result