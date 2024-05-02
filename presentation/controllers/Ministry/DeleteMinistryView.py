from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from application.useCases.DeleteMinistry.DeleteMinistry import DeleteMinistry
from application.useCases.DeleteMinistry.protocols.DeleteMinistryRequest import DeleteMinistryRequest


class DeleteMinistryView(APIView):
    def delete(self, request, id):
        try:
            # Building inbound
            inbound = DeleteMinistryRequest()
            inbound.id = id

            # Calling use case
            useCase = DeleteMinistry()
            result = useCase.execute(inbound)

            # Serializing
            outbound = result.__dict__

            return Response({"data": outbound}, status=status.HTTP_200_OK)

        except Exception as e:
            import traceback
            traceback.print_exc()
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)