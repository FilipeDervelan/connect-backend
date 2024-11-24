from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from application.useCases.UpdateUser.UpdateUser import UpdateUser
from application.useCases.UpdateUser.protocols.UpdateUserRequest import (
    UpdateUserRequest,
)


class UpdateUserView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request: Request, id: int) -> Response:
        try:
            inbound = UpdateUserRequest()
            inbound.id = id
            inbound.name = request.data.get("name")
            inbound.birth_day = request.data.get("birth_day")

            useCase = UpdateUser()
            result = useCase.execute(inbound)

            outbound = result.__dict__

            return Response(outbound, status=status.HTTP_200_OK)

        except Exception as e:
            import traceback

            traceback.print_exc()
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
