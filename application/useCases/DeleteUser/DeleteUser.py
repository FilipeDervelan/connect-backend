from app.models import CustomUser

from application.useCases.DeleteUser.protocols.DeleteUserRequest import (
    DeleteUserRequest,
)
from application.useCases.DeleteUser.protocols.DeleteUserResponse import (
    DeleteUserResponse,
)


class DeleteUser:
    def execute(self, inbound: DeleteUserRequest) -> DeleteUserResponse:
        result = DeleteUserResponse()

        try:
            user = CustomUser.objects.get(id=inbound.id)

            user.delete()

            result.response = "User deleted"
            result.status = 200

        except CustomUser.DoesNotExist:
            result.response = "User not found"
            result.status = 400

        except Exception as e:
            result.response = str(e)
            result.status = 500

        return result
