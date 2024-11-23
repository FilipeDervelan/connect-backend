from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from application.useCases.CreateFunction.CreateFunction import CreateFunction
from application.useCases.CreateFunction.protocols.CreateFunctionRequest import (
    CreateFunctionRequest,
)


class CreateFunctionView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            # Building inbound
            inbound = CreateFunctionRequest()
            inbound.name = request.data.get("name")
            inbound.description = request.data.get("description")
            inbound.ministry_id = request.data.get("ministry_id")

            # Calling use case
            useCase = CreateFunction()
            result = useCase.execute(inbound)

            # Serializing
            outbound = result.__dict__

            return Response(
                {"data": outbound},
                status=status.HTTP_201_CREATED,
            )

        except Exception as e:
            import traceback

            traceback.print_exc()
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
