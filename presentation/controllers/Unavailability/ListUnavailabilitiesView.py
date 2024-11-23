from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from application.useCases.ListUnavailabilities.ListUnavailabilities import (
    ListUnavailabilities,
)


class ListUnavailabilitiesView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        useCase = ListUnavailabilities()
        result = useCase.execute()

        outbound = result.__dict__

        return Response({"data": outbound}, status=status.HTTP_200_OK)
