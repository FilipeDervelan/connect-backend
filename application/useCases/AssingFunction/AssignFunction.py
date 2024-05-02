from app.models import Function, User
from application.useCases.AssingFunction.protocols.AssignFunctionRequest import AssignFunctionRequest
from application.useCases.AssingFunction.protocols.AssignFunctionResponse import AssignFunctionResponse


class AssignFunction:
    def execute(self, inbound: AssignFunctionRequest) -> AssignFunctionResponse:
        user = User.objects.get(id=inbound.user_id)
        function = Function.objects.get(id=inbound.function_id)

        result = AssignFunctionResponse()

        # Verifying if user already joined in the function ministry
        if not user.ministry.exists() or not user.ministry.filter(id=function.ministry.id).exists():
            result.response = f"User needs enter on {function.ministry.name} ministry first"
            result.status = 400

            return result

        user.function.add(function)

        result.response = "Function assigned"
        result.status = 200

        return result
