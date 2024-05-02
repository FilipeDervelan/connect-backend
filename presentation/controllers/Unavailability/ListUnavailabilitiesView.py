from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from application.useCases.ListUnavailabilities.ListUnavailabilities import ListUnavailabilities
from application.useCases.ListUnavailabilities.protocols.ListUnavailabilitiesRequest import ListUnavailabilitiesRequest


class ListUnavailabilitiesView(APIView):
    def get(self, request):
        inbound = ListUnavailabilitiesRequest()
        inbound.request = "GET"

        useCase = ListUnavailabilities()
        result = useCase.execute(inbound)

        outbound = result.__dict__

        return Response({"data": outbound}, status=status.HTTP_200_OK)