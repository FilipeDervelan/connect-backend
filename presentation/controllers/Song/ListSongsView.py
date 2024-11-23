from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from application.useCases.ListSongs.ListSongs import ListSongs


class ListSongsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request) -> Response:
        use_case = ListSongs()
        result = use_case.execute()

        return Response(result.response, status=result.status)
