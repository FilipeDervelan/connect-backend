from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from application.useCases.UpdateMinistry.UpdateMinistry import UpdateMinistry
from application.useCases.UpdateMinistry.protocols.UpdateMinistryRequest import (
    UpdateMinistryRequest,
)


class UpdateMinistryView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request: Request, id: str) -> Response:
        try:
            inbound = UpdateMinistryRequest()
            inbound.id = id
            inbound.name = request.data.get("name")
            inbound.description = request.data.get("description")

            useCase = UpdateMinistry()
            result = useCase.execute(inbound)

            outbound = result.__dict__

            return Response(outbound, status=status.HTTP_200_OK)

        except Exception as e:
            import traceback

            traceback.print_exc()
            return Response(
                str(e),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
