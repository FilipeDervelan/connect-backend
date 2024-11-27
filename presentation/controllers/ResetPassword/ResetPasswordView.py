from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from application.useCases.ResetPassword.protocols.ResetPasswordRequest import (
    ResetPasswordRequest,
)
from application.useCases.ResetPassword.ResetPassword import ResetPassword


@api_view(["POST"])
@permission_classes([AllowAny])
def reset_password(request: Request) -> Response:

    reset_password_request = ResetPasswordRequest(email=request.data["email"])
    reset_password = ResetPassword()

    try:
        reset_password.execute(reset_password_request)
        return Response(status=status.HTTP_204_NO_CONTENT)

    except Exception as e:
        return Response(
            str(e),
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
