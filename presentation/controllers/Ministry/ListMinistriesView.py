from rest_framework.views import APIView
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from application.useCases.ListMinistries.ListMinistries import ListMinistries


class ListMinistriesView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request) -> Response:
        useCase = ListMinistries()
        result = useCase.execute()

        outbound = result.response

        return Response(outbound, status=status.HTTP_200_OK)
