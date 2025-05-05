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
            inbound = CreateMinistryRequest()
            inbound.name = request.data.get("name")
            inbound.description = request.data.get("description")
            inbound.user_id = request.user.id

            use_case = CreateMinistry()
            result = use_case.execute(inbound)

            if result.status == 400:
                return Response(
                    result.response,
                    status=result.status,
                )

            outbound = result.response

            return Response(
                outbound,
                status=status.HTTP_201_CREATED,
            )

        except Exception as e:
            return Response(
                str(e),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
