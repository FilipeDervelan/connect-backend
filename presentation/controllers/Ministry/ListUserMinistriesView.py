from rest_framework.views import APIView
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

# from rest_framework.permissions import IsAuthenticated

from application.useCases.ListMinistries.ListMinistries import ListMinistries
from application.useCases.ListUserMinistries.ListUserMinistries import (
    ListUserMinistries,
)
from application.useCases.ListUserMinistries.protocols.ListUserMinistriesRequest import (
    ListUserMinistriesRequest,
)


class ListUserMinistriesView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request: Request) -> Response:
        try:
            inbound = ListUserMinistriesRequest()
            inbound.id = request.user.id

            user_case = ListUserMinistries()
            result = user_case.execute(inbound)

            outbound = result.response

            return Response(outbound, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                str(e),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
