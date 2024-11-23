from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from application.useCases.ListScales.ListScales import ListScales
from application.useCases.ListScales.protocols.ListScalesRequest import (
    ListScalesRequest,
)


class ListScalesView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        inbound = ListScalesRequest()
        inbound.request = "GET"

        useCase = ListScales()
        result = useCase.execute(inbound)

        outbound = result.__dict__

        return Response(outbound, status=status.HTTP_200_OK)
