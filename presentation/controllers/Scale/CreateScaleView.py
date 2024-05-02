from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from application.useCases.CreateScale.CreateScale import CreateScale
from application.useCases.CreateScale.protocols.CreateScaleRequest import CreateScaleRequest

class CreateScaleView(APIView):
    def post(self, request):
        # Building inbound
        inbound = CreateScaleRequest()
        inbound.name = request.data.get("name")
        inbound.description = request.data.get("description")
        inbound.date = request.data.get("date")
        inbound.participants = request.data.get("participants")
        inbound.function = request.data.get("function")
        inbound.song = request.data.get("songs")
        inbound.ministry_id = request.data.get("ministry_id")

        # Calling use case
        useCase = CreateScale()
        result = useCase.execute(inbound)

        # Serializing
        outbound = result.__dict__

        return Response({"data": outbound}, status=status.HTTP_201_CREATED)
