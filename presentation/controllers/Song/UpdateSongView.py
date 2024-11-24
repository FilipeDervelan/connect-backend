from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from application.useCases.UpdateSong.UpdateSong import UpdateSong
from application.useCases.UpdateSong.protocols.UpdateSongRequest import (
    UpdateSongRequest,
)


class UpdateSongView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request: Request, id: int) -> Response:
        try:
            inbound = UpdateSongRequest()
            inbound.id = id
            inbound.name = request.data.get("name") if "name" in request.data else None
            inbound.description = (
                request.data.get("description")
                if "desscription" in request.data
                else None
            )
            inbound.link = request.data.get("link") if "link" in request.data else None
            inbound.singer_id = (
                request.data.get("singer_id") if "singer_id" in request.data else None
            )

            use_case = UpdateSong()
            outbound = use_case.execute(inbound)

            return Response(outbound.response, status=outbound.status)

        except Exception as e:
            return Response(
                str(e),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
