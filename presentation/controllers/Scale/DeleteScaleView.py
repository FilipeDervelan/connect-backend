from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from application.useCases.DeleteScale.DeleteScale import DeleteScale
from application.useCases.DeleteScale.protocols.DeleteScaleRequest import DeleteScaleRequest


class DeleteScaleView(APIView):
    def delete(self, request, id):
        inbound = DeleteScaleRequest()
        inbound.id = id

        useCase = DeleteScale()
        result = useCase.execute(inbound)

        outbound = result.__dict__

        return Response({"data": outbound}, status=status.HTTP_200_OK)