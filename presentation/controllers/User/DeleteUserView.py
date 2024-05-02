from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from application.useCases.DeleteUser.DeleteUser import DeleteUser
from application.useCases.DeleteUser.protocols.DeleteUserRequest import DeleteUserRequest

class DeleteUserView(APIView):
    def delete(self, request, id):
        # Building inbound
        inbound = DeleteUserRequest()
        inbound.id = id

        # Calling use case
        useCase = DeleteUser()
        result = useCase.execute(inbound)

        # Serializing
        outbound = result.__dict__

        return Response({"data": outbound}, status=status.HTTP_200_OK)
