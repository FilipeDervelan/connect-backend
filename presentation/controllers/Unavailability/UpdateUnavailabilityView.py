from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from application.useCases.UpdateUnavailability.UpdateUnavailability import (
    UpdateUnavailability,
)
from application.useCases.UpdateUnavailability.protocols.UpdateUnavailabilityRequest import (
    UpdateUnavailabilityRequest,
)


class UpdateUnavailabilityView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request: Request, id: str) -> Response:
        inbound = UpdateUnavailabilityRequest()
        inbound.id = id
        inbound.start_date = request.data.get("start_date")
        inbound.end_date = request.data.get("end_date")

        useCase = UpdateUnavailability()
        result = useCase.execute(inbound)

        outbound = result.__dict__

        return Response({"data": outbound}, status=status.HTTP_200_OK)
