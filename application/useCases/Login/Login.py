from typing import Any
from django.contrib.auth import authenticate
from .protocols.LoginResponse import LoginResponse


class Login:
    """
    Service that executes the login operation.
    """

    def execute(self, request: Any) -> LoginResponse:
        """
        Executes the login operation.

        Args:
            request (Any): The request object containing username and password.

        Returns:
            LoginResponse: An instance of LoginResponse indicating the
                success of the login operation.
        """

        user = authenticate(
            username=request.username,
            password=request.password,
        )

        if user is not None:
            return LoginResponse(success=True, user=user)
        else:
            return LoginResponse(success=False)
