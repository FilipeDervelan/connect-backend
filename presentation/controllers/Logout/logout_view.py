from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from application.useCases.Logout.logout import Logout
from application.useCases.Logout.protocols.logout_request import LogoutRequest


class LogoutView(APIView):
    def post(self, request: Request) -> Response:
        try:
            inbound = LogoutRequest()
            inbound.token = request.data["refresh_token"]

            use_case = Logout()
            outbound = use_case.execute(inbound)

            return Response(status=outbound.status)

        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
