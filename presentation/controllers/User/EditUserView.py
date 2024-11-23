from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from application.useCases.EditUser.EditUser import EditUser
from application.useCases.EditUser.protocols.EditUserRequest import EditUserRequest


class EditUserView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, id):
        try:
            # Building inbound
            inbound = EditUserRequest()
            inbound.id = id
            inbound.name = request.data.get("name")
            inbound.birth_day = request.data.get("birth_day")

            # Calling use case
            useCase = EditUser()
            result = useCase.execute(inbound)

            # Serializing
            outbound = result.__dict__

            return Response({"data": outbound}, status=status.HTTP_200_OK)

        except Exception as e:
            import traceback

            traceback.print_exc()
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
