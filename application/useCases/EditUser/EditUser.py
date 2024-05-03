from datetime import datetime
from app.models import User
from application.useCases.EditUser.protocols.EditUserRequest import EditUserRequest
from application.useCases.EditUser.protocols.EditUserResponse import EditUserResponse


class EditUser:
    def execute(self, inbound: EditUserRequest) -> EditUserResponse:
        # Recovering user
        user = User.objects.get(id=inbound.id)

        birth_day = datetime.strptime(inbound.birth_day, '%d/%m/%Y')
        birth_day = birth_day.strftime('%Y-%m-%d')

        user.name = inbound.name
        user.birth_day = birth_day
        user.updated_at = datetime.now()

        user.save()

        result = EditUserResponse()
        result.response = "User edited"
        result.status = 200

        return result

