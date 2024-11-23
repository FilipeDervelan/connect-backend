from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from application.useCases.CreateUnavailability.CreateUnavailability import (
    CreateUnavailability,
)
from application.useCases.CreateUnavailability.protocols.CreateUnavailabilityRequest import (
    CreateUnavailabilityRequest,
)


class CreateUnavailabilityView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        inbound = CreateUnavailabilityRequest()
        inbound.start_date = request.data.get("start_date")
        inbound.end_date = request.data.get("end_date")
        inbound.user_id = request.data.get("user_id")

        useCase = CreateUnavailability()
        result = useCase.execute(inbound)

        outbound = result.__dict__

        return Response({"data": outbound}, status=status.HTTP_201_CREATED)
