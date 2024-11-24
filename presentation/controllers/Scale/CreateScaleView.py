from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from application.useCases.CreateScale.CreateScale import CreateScale
from application.useCases.CreateScale.protocols.CreateScaleRequest import (
    CreateScaleRequest,
)


class CreateScaleView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request: Request) -> Response:
        try:
            inbound = CreateScaleRequest()
            inbound.name = request.data.get("name")
            inbound.description = request.data.get("description")
            inbound.date = request.data.get("date")
            inbound.participants = request.data.get("participants")
            inbound.song = request.data.get("songs")
            inbound.ministry_id = request.data.get("ministry_id")

            useCase = CreateScale()
            result = useCase.execute(inbound)

            outbound = result.__dict__

            return Response(outbound, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(
                str(e),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
