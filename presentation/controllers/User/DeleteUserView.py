from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from application.useCases.DeleteUser.DeleteUser import DeleteUser
from application.useCases.DeleteUser.protocols.DeleteUserRequest import (
    DeleteUserRequest,
)


class DeleteUserView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request: Request, id: int) -> Response:
        inbound = DeleteUserRequest()
        inbound.id = id

        useCase = DeleteUser()
        result = useCase.execute(inbound)

        outbound = result.__dict__

        return Response(outbound, status=status.HTTP_200_OK)
