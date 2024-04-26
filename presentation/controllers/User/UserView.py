import datetime
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from app.models import Function, Ministry, User

class UserView(APIView):
    def post(self, payload):
        print("create user")

        userName = payload.data.get("name")
        password = payload.data.get("password")
        birthDayRequest = payload.data.get("birth_day")
        email = payload.data.get("email")
        functionId = payload.data.get("function_id")
        ministryId = payload.data.get("ministry_id")

        birthDay = datetime.datetime.strptime(birthDayRequest, "%d/%m/%Y").strftime("%Y-%m-%d")

        functionRecovered = Function.models.get(id=functionId)
        ministryRecovered = Ministry.models.get(id=ministryId)

        if not userName:
            return Response({"message": "Name is required"}, status=status.HTTP_400_BAD_REQUEST)

        if not password:
            return Response({"message": "Password is required"}, status=status.HTTP_400_BAD_REQUEST)

        if len(password) < 8:
            return Response({"message": "Minimum password length is 8 characters"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not email:
            return Response({"message": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

        newUser = User(name=userName, password=password, email=email, date_of_birth=birthDay, function=functionRecovered, ministry=ministryRecovered)

        newUser.save()

        return Response({"message": "Succesfully Created!"}, status=status.HTTP_201_CREATED)

    def delete(self, request, id):
        print("delete user")

        user = User.objects.get(id=id)

        user.delete()

        return Response({"message": "User deleted"}, status=status.HTTP_200_OK)
