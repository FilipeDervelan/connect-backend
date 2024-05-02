from app.models import User
from application.useCases.DeleteUser.protocols.DeleteUserRequest import DeleteUserRequest
from application.useCases.DeleteUser.protocols.DeleteUserResponse import DeleteUserResponse


class DeleteUser:
    def execute(self, inbound: DeleteUserRequest) -> DeleteUserResponse:
        result = DeleteUserResponse()

        try:
            user = User.objects.get(id=inbound.id)

        except:
            result.response = "User not found"
            result.status = 400
            return result

        user.delete()

        result.response = "User deleted"
        result.status = 200

        return result
