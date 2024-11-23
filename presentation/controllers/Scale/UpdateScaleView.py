from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from application.useCases.UpdateScale.UpdateScale import UpdateScale
from application.useCases.UpdateScale.protocols.UpdateScaleRequest import (
    UpdateScaleRequest,
)


class UpdateScaleView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, id):
        inbound = UpdateScaleRequest()
        inbound.id = id
        inbound.name = request.data.get("name")
        inbound.description = request.data.get("description")
        inbound.date = request.data.get("date")
        inbound.songs = request.data.get("songs")
        inbound.participants = request.data.get("participants")
        inbound.ministry_id = request.data.get("ministry_id")

        useCase = UpdateScale()
        result = useCase.execute(inbound)

        outbound = result.__dict__

        return Response({"data": outbound}, status=status.HTTP_200_OK)
