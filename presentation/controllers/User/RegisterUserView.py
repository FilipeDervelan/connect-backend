from application.useCases.RegisterUser.RegisterUser import RegisterUser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response





class RegisterUserView(APIView):
    def post(self, request: Request) -> Response:
        try:
            use_case = RegisterUser()
            outbound = use_case.execute(request.data)

            return Response(
                outbound.message,
                status=outbound.status,
            )

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
