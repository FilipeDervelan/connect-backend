from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from application.useCases.UpdateFunction.UpdateFunction import UpdateFunction
from application.useCases.UpdateFunction.protocols.UpdateFunctionRequest import (
    UpdateFunctionRequest,
)


class UpdateFunctionView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, id):
        try:
            # Building inbound
            inbound = UpdateFunctionRequest()
            inbound.id = id
            inbound.name = request.data.get("name")
            inbound.description = request.data.get("description")
            inbound.ministry_id = request.data.get("ministry_id")

            # Calling use case
            useCase = UpdateFunction()
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
