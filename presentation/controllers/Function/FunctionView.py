from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from app.models import Function

class FunctionView(APIView):
    def post(self, request):
        print("Create Function")

        name = request.data.get("name")
        description = request.data.get("description")

        if not name:
            return Response({"message": "Name is required"}, status=status.HTTP_400_BAD_REQUEST)

        newFunction = Function(name=name, description=description)

        newFunction.save()

        return Response({"message": "Function Created!"}, status=status.HTTP_201_CREATED)

    # def put(self, request, id):
    #     print("edit function")

    #     name = request.data.get("name")
    #     description = request.data.get("description")

