from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from application.useCases.Login.protocols.LoginRequest import LoginRequest
from application.useCases.Login.Login import Login


@api_view(["POST"])
@permission_classes([AllowAny])
def login(request: Request) -> Response:
    """
    Handles the login functionality by authenticating the user's credentials
    and generating access and refresh tokens.
    """

    login_request = LoginRequest(
        username=request.data.get("username"),
        password=request.data.get("password"),
    )

    if not login_request.username or not login_request.password:
        return Response(
            "Invalid credentials",
            status=status.HTTP_401_UNAUTHORIZED,
        )

    login_use_case = Login()
    login_response = login_use_case.execute(login_request)

    if login_response.success:
        refresh = RefreshToken.for_user(login_response.user)

        response = Response(
            {
                "access": str(refresh.access_token),
                "refresh_token": str(refresh),
                "username": login_response.user.username,
                "email": login_response.user.email,
            }
        )
        return response

    else:
        return Response(
            "Invalid credentials",
            status=status.HTTP_401_UNAUTHORIZED,
        )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def verify_token(request: Request) -> Response:
    """
    Function that's verify if user token is valid
    """

    return Response({"detail": "Token is valid."}, status=200)
