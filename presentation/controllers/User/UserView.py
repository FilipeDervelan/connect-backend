from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class UserView(APIView):
    def post(self, payload):
        print("create user")

        return Response("Created", status=status.HTTP_201_CREATED)