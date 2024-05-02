from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from application.useCases.UpdateMinistry.UpdateMinistry import UpdateMinistry
from application.useCases.UpdateMinistry.protocols.UpdateMinistryRequest import UpdateMinistryRequest


class UpdateMinistryView(APIView):
    def put(self, request, id):
        try:
            # Building inbound
            inbound = UpdateMinistryRequest()
            inbound.id = id
            inbound.name = request.data.get("name")
            inbound.description = request.data.get("description")

            # Calling use case
            useCase = UpdateMinistry()
            result = useCase.execute(inbound)

            # Serializing
            outbound = result.__dict__

            return Response({"data": outbound}, status=status.HTTP_200_OK)

        except Exception as e:
            import traceback
            traceback.print_exc()
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
