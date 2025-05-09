from datetime import datetime
from rest_framework import status
from rest_framework import serializers
from django.contrib.auth import get_user_model

from app.models import CustomUser
from application.useCases.RegisterUser.protocols.RegisterUserRequest import (
    RegisterUserRequest,
)
from application.useCases.RegisterUser.protocols.RegisterUserResponse import (
    RegisterUserResponse,
)


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "birth_day",
            "function",
            "ministry",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = User(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            birth_day=validated_data["birth_day"],
        )
        user.set_password(password)
        user.save()

        return user


class RegisterUser:
    def execute(self, inbound: dict) -> RegisterUserResponse:
        outbound = RegisterUserResponse()

        user_email = CustomUser.objects.filter(email=inbound["email"])

        if user_email.exists():
            outbound.message = "Email already registered"
            outbound.status = 400

            return outbound

        if "birth_day" in inbound:
            inbound["birth_day"] = datetime.fromisoformat(
                inbound["birth_day"].replace("Z", "+00:00")
            ).date()

        serializer = RegisterUserRequest(data=inbound)

        if not serializer.is_valid():
            outbound.message = serializer.errors
            outbound.status = status.HTTP_400_BAD_REQUEST
            return outbound

        user_serializer = UserSerializer(data=serializer.validated_data)
        if user_serializer.is_valid():
            user_serializer.save()
            outbound.message = "User created successfully!"
            outbound.status = status.HTTP_201_CREATED
        else:
            message = user_serializer.errors

            if "username" in message:
                outbound.message = user_serializer.errors["username"][0]
            else:
                outbound.message = user_serializer.errors

            outbound.status = status.HTTP_400_BAD_REQUEST

        return outbound
