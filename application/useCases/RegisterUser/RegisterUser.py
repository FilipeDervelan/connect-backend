from rest_framework import status
from rest_framework import serializers
from django.contrib.auth import get_user_model

from application.useCases.register_user.protocols.register_user_request import (
    RegisterUserRequest,
)
from application.useCases.register_user.protocols.register_user_response import (
    RegisterUserResponse,
)


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True
    )  # Para não expor o password na resposta

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
            "password": {
                "write_only": True
            },  # Apenas para escrita, nunca será retornado
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
        user.set_password(password)  # Garante que o password seja salvo de forma segura
        user.save()

        return user


class RegisterUser:
    def execute(self, inbound: dict) -> RegisterUserResponse:
        outbound = RegisterUserResponse()

        # Validação usando RegisterUserRequest
        serializer = RegisterUserRequest(data=inbound)

        if not serializer.is_valid():
            outbound.message = serializer.errors
            outbound.status = status.HTTP_400_BAD_REQUEST
            return outbound

        # Criação do usuário
        user_serializer = UserSerializer(data=serializer.validated_data)
        if user_serializer.is_valid():
            user_serializer.save()
            outbound.message = "User created successfully!"
            outbound.status = status.HTTP_201_CREATED
        else:
            outbound.message = user_serializer.errors
            outbound.status = status.HTTP_400_BAD_REQUEST

        return outbound
