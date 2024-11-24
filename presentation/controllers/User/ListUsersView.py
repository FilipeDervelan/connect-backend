from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from application.useCases.ListUsers.ListUsers import ListUsers


class ListUsersView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request) -> Response:
        use_case = ListUsers()
        outbound = use_case.execute()

        return Response(outbound.response, status=status.HTTP_200_OK)
