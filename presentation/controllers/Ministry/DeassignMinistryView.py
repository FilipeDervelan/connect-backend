from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from application.useCases.DeassignMinistry.DeassignMinistry import DeassignMinistry
from application.useCases.DeassignMinistry.protocols.DeassignMinistryRequest import (
    DeassignMinistryRequest,
)


class DeassignMinistryView(APIView):
    permission_classes = (IsAuthenticated,)

    def patch(self, request: Request) -> Response:
        try:
            inbound = DeassignMinistryRequest()
            inbound.user_id = request.data.get("user_id")
            inbound.ministry_id = request.data.get("ministry_id")

            useCase = DeassignMinistry()
            result = useCase.execute(inbound)

            outbound = result.__dict__

            return Response(outbound, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                str(e),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
