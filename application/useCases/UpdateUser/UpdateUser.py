from datetime import datetime
from app.models import CustomUser
from application.useCases.UpdateUser.protocols.UpdateUserRequest import (
    UpdateUserRequest,
)
from application.useCases.UpdateUser.protocols.UpdateUserResponse import (
    UpdateUserResponse,
)


class UpdateUser:
    def execute(self, inbound: UpdateUserRequest) -> UpdateUserResponse:
        user = CustomUser.objects.get(id=inbound.id)

        birth_day = datetime.strptime(inbound.birth_day, "%d/%m/%Y")
        birth_day = birth_day.strftime("%Y-%m-%d")

        user.username = inbound.name
        user.birth_day = birth_day
        user.updated_at = datetime.now()

        user.save()

        result = UpdateUserResponse()
        result.response = "User updated"
        result.status = 200

        return result
