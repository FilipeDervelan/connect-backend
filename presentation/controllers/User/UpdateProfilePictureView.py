from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from application.useCases.UpdateProfilePicture.UpdateProfilePicture import (
    UpdateProfilePicture,
)
from infra.serializers.user_serializer import CustomUserSerializer


class UpdateProfilePictureView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, uid):
        try:
            user = request.user
            profile_picture = request.FILES.get("image")

            if not profile_picture:
                return Response(
                    "No image uploaded",
                    status=status.HTTP_400_BAD_REQUEST,
                )

            updated_user = UpdateProfilePicture.execute(user, profile_picture)
            serializer = CustomUserSerializer(updated_user)

            return Response(serializer.data)

        except Exception as e:
            return Response(
                str(e),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
