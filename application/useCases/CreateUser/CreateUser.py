from app.models import User
from application.useCases.CreateUser.protocols.CreateUserRequest import CreateUserRequest
from application.useCases.CreateUser.protocols.CreateUserResonse import CreateUserResponse


class CreateUser:
    def execute(self, inbound: CreateUserRequest) -> CreateUserResponse:
        result = CreateUserResponse()

        # Verifying if required params exists
        if not inbound.name:
            result.response = "Name is required"
            result.status = 400

            return result

        if not inbound.email:
            result.response = "Email is required"
            result.status = 400

            return result

        if not inbound.password:
            result.response = "Password is required"
            result.status = 400

            return result

        # Transfering the inbound properties value to variables
        name = inbound.name
        email = inbound.email
        password = inbound.password
        birth_day = inbound.birth_day if inbound.birth_day else None

        # Creating user
        newUser = User(name=name, email=email, password=password, birth_day=birth_day)

        newUser.save()

        result.response = "Successfully Created"
        result.status = 201

        return result
