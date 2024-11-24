from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from application.useCases.CreateSinger.CreateSinger import CreateSinger
from application.useCases.CreateSinger.protocols.CreateSingerRequest import (
    CreateSingerRequest,
)


class CreateSingerView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request: Request) -> Response:
        try:
            inbound = CreateSingerRequest()
            inbound.name = request.data.get("name") if "name" in request.data else None

            if not inbound.name:
                return Response(
                    "Name is required",
                    status=status.HTTP_400_BAD_REQUEST,
                )

            use_case = CreateSinger()
            outbound = use_case.execute(inbound)

            return Response(outbound.response, status=outbound.status)

        except Exception as e:
            return Response(
                str(e),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
