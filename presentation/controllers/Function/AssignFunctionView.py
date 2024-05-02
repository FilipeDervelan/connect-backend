from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from application.useCases.AssingFunction.AssignFunction import AssignFunction
from application.useCases.AssingFunction.protocols.AssignFunctionRequest import AssignFunctionRequest


class AssignFunctionView(APIView):
    def post(self, request):
        try:
            # Building inboumd
            inbound = AssignFunctionRequest()
            inbound.user_id = request.data.get("user_id")
            inbound.function_id = request.data.get("function_id")

            # Calling use case
            useCase = AssignFunction()
            result = useCase.execute(inbound)

            # Serializing
            outbound = result.__dict__

            return Response({"data": outbound}, status=status.HTTP_200_OK)

        except Exception as e:
            import traceback
            traceback.print_exc()
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)