from app.models import CustomUser
from application.useCases.GetUser.protocols.GetUserRequest import GetUserRequest
from application.useCases.GetUser.protocols.GetUserResponse import GetUserResponse


class GetUser:
    def execute(self, inbound: GetUserRequest) -> GetUserResponse:
        outbound = GetUserResponse()

        user = CustomUser.objects.get(id=inbound.id)

        result = {
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "birth_date": user.birth_day,
            "created_at": user.created_at.strftime("%d/%m/%Y"),
        }

        outbound.response = result

        return outbound
