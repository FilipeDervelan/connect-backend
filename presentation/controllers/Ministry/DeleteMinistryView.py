from rest_framework.views import APIView
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from application.useCases.DeleteMinistry.DeleteMinistry import DeleteMinistry
from application.useCases.DeleteMinistry.protocols.DeleteMinistryRequest import (
    DeleteMinistryRequest,
)


class DeleteMinistryView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request: Request, id: str) -> Response:
        try:
            inbound = DeleteMinistryRequest()
            inbound.id = id

            useCase = DeleteMinistry()
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
