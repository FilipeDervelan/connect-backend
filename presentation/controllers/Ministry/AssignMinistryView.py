from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from application.useCases.AssignMinistry.AssignMinistry import AssignMinistry
from application.useCases.AssignMinistry.protocols.AssignMinistryRequest import (
    AssignMinistryRequest,
)


class AssignMinistryView(APIView):
    permission_classes = (IsAuthenticated,)

    def patch(self, request):
        # Building inbound
        inbound = AssignMinistryRequest()
        inbound.user_id = request.data.get("user_id")
        inbound.ministry_id = request.data.get("ministry_id")

        # Calling use case
        useCase = AssignMinistry()
        result = useCase.execute(inbound)

        # Serializing
        outbound = result.__dict__

        return Response(outbound, status=status.HTTP_200_OK)
