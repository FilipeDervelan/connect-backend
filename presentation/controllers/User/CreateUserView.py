import datetime
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from application.useCases.CreateUser.CreateUser import CreateUser
from application.useCases.CreateUser.protocols.CreateUserRequest import CreateUserRequest

class CreateUserView(APIView):
    def post(self, request):
        try:
            # Building inbound
            inbound = CreateUserRequest()
            inbound.name = request.data.get("name")
            inbound.email = request.data.get("email")
            inbound.password = request.data.get("password")
            inbound.birth_day = request.data.get("birth_day")

            # Calling use case
            useCase = CreateUser()
            result = useCase.execute(inbound)

            # Serializing
            outbound = result.__dict__

            return Response({"data": outbound}, status=status.HTTP_201_CREATED)

        except Exception as e:
            import traceback
            traceback.print_exc()
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
