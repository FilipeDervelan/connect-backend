from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from application.useCases.DeleteUnavailability.DeleteUnavailability import (
    DeleteUnavailability,
)
from application.useCases.DeleteUnavailability.protocols.DeleteUnavailabilityRequest import (
    DeleteUnavailabilityRequest,
)


class DeleteUnavailabilityView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request: Request, id: int) -> Response:
        try:
            inbound = DeleteUnavailabilityRequest()
            inbound.id = id

            use_case = DeleteUnavailability()
            result = use_case.execute(inbound)

            return Response(result.response, status=result.status)

        except Exception as e:
            return Response(
                str(e),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
