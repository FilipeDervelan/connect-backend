from rest_framework import serializers


class RegisterUserRequest(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(
        max_length=30,
        required=False,
        allow_blank=True,
    )
    last_name = serializers.CharField(
        max_length=150,
        required=False,
        allow_blank=True,
    )
    birth_day = serializers.DateField(required=False, allow_null=True)
    function = serializers.ListField(
        child=serializers.IntegerField(), required=False, allow_empty=True
    )
    ministry = serializers.ListField(
        child=serializers.IntegerField(), required=False, allow_empty=True
    )

    def validate(self, data):
        # Validações customizadas (exemplo)
        if "username" in data and data["username"].lower() == "admin":
            raise serializers.ValidationError("The username 'admin' is not allowed.")
        return data

    def to_internal_value(self, data):
        """
        Opcional: converte os dados antes de serem usados.
        """
        data["username"] = data["username"].strip()
        return super().to_internal_value(data)
