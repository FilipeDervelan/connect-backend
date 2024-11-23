from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from application.useCases.Logout.protocols.logout_request import LogoutRequest
from application.useCases.Logout.protocols.logout_response import LogoutResponse


class Logout:
    permission_classes = (IsAuthenticated,)

    def execute(self, inbound: LogoutRequest) -> LogoutResponse:
        try:
            outbound = LogoutResponse()
            outbound.status = 205

            refresh_token = inbound.token
            token = RefreshToken(refresh_token)
            token.blacklist()

            return outbound

        except Exception:
            outbound.status = 400

            return outbound
