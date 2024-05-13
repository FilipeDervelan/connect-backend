from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from application.useCases.ListMinistries.ListMinistries import ListMinistries
from application.useCases.ListMinistries.protocols.ListMinistriesRequest import ListMinistriesRequest


class ListMinistriesView(APIView):
    def get(self, request):
        print("List ministries")
        inbound = ListMinistriesRequest()
        inbound.request = ""

        useCase = ListMinistries()
        result = useCase.execute(inbound)

        outbound = result.__dict__

        return Response({"data": outbound}, status=status.HTTP_200_OK)