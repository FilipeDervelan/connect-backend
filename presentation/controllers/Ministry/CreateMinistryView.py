from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from application.useCases.CreateMinistry.CreateMinistry import CreateMinistry
from application.useCases.CreateMinistry.protocols.CreateMinistryRequest import (
    CreateMinistryRequest,
)


class CreateMinistryView(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            # Building inbound
            inbound = CreateMinistryRequest()
            inbound.name = request.data.get("name")
            inbound.description = request.data.get("description")
            inbound.user_id = request.user.id

            use_case = CreateMinistry()
            result = use_case.execute(inbound)

            outbound = result.__dict__

            return Response(outbound, status=status.HTTP_201_CREATED)

        except Exception as e:
            import traceback

            traceback.print_exc()
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
