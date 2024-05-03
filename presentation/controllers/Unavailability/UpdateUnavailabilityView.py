from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from application.useCases.UpdateUnavailability.UpdateUnavailability import UpdateUnavailability
from application.useCases.UpdateUnavailability.protocols.UpdateUnavailabilityRequest import UpdateUnavailabilityRequest


class UpdateUnavailabilityView(APIView):
    def put(self, request, id):
        inbound = UpdateUnavailabilityRequest()
        inbound.id = id
        inbound.start_date = request.data.get("start_date")
        inbound.end_date = request.data.get("end_date")

        useCase = UpdateUnavailability()
        result = useCase.execute(inbound)

        outbound = result.__dict__

        return Response({"data": outbound}, status=status.HTTP_200_OK)