from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from application.useCases.GetUser.GetUser import GetUser
from application.useCases.GetUser.protocols.GetUserRequest import GetUserRequest


class GetUserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request, id: int) -> Response:
        try:
            inbound = GetUserRequest()
            inbound.id = id

            use_case = GetUser()
            outbound = use_case.execute(inbound)

            return Response(outbound.response, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                str(e),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
