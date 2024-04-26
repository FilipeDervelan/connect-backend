from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app.models import Ministry

class MinistryView(APIView):
    def post(self, request):
        print("create ministry")

        name = request.data.get("name")
        description = request.data.get("description")

        if not name:
            return Response({"message": "Name is required"}, status=status.HTTP_400_BAD_REQUEST)

        newMinistry = Ministry(name=name, description=description)

        newMinistry.save()

        return Response({"message": "Successfully created"}, status=status.HTTP_201_CREATED)
