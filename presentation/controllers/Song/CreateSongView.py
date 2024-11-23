from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from application.useCases.CreateSong.CreateSong import CreateSong
from application.useCases.CreateSong.protocols.CreateSongRequest import (
    CreateSongRequest,
)


class CreateSongView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request: Request) -> Response:
        try:
            inbound = CreateSongRequest()
            inbound.name = request.data.get("name")
            inbound.description = request.data.get("description")
            inbound.link = request.data.get("link")
            inbound.singer = request.data.get("singer")

            useCase = CreateSong()
            result = useCase.execute(inbound)

            outbound = result.__dict__

            return Response(outbound, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(
                str(e),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
