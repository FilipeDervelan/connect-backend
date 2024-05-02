from datetime import datetime
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

        if birth_day:
            birth_day = datetime.strptime(birth_day, '%d/%m/%Y')
            birth_day = birth_day.strftime('%Y-%m-%d')

        # Creating user
        newUser = User(name=name, email=email, password=password, birth_day=birth_day)

        newUser.save()

        result.response = "Successfully Created"
        result.status = 201

        return result
