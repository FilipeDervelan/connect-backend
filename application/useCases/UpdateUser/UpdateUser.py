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

        date_str = inbound.birth_date.split("T")[0]

        birth_date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        birth_date = birth_date_obj.strftime("%Y-%m-%d")

        user.username = inbound.username.strip()
        user.first_name = inbound.first_name.strip()
        user.last_name = inbound.last_name.strip()
        user.birth_day = birth_date
        user.updated_at = datetime.now()

        user.save()

        result = UpdateUserResponse()
        result.response = "User updated"
        result.status = 200

        return result
