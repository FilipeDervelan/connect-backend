from app.models import Function, Ministry
from application.useCases.CreateFunction.protocols.CreateFunctionRequest import CreateFunctionRequest
from application.useCases.CreateFunction.protocols.CreateFunctionResponse import CreateFunctionResponse

class CreateFunction:
    def execute(self, inbound: CreateFunctionRequest) -> CreateFunctionResponse:
        name = inbound.name
        description = inbound.description
        ministry_id = inbound.ministry_id

        ministry = Ministry.objects.get(id=ministry_id)

        newFunction = Function(name=name, description=description, ministry=ministry)

        newFunction.save()

        result = CreateFunctionResponse()
        result.response = "Function successfully created"
        result.status = 201

        return result
