from app.models import CustomUser
from application.useCases.ListUsers.protocols.ListUsersResponse import ListUsersResponse


class ListUsers:
    def execute(self) -> ListUsersResponse:
        outbound = ListUsersResponse()

        result = []

        users = CustomUser.objects.all()

        for user in users:
            result.append(
                {
                    "id": user.pk,
                    "username": user.username,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "birth_day": user.birth_day,
                    "last_login": user.last_login,
                    "ministries": [
                        {
                            "id": ministry.id,
                            "name": ministry.name,
                            "description": ministry.description,
                            "owner_id": ministry.owner_id,
                            "created_at": ministry.created_at,
                        }
                        for ministry in user.ministry.all()
                    ],
                    "functions": [
                        {
                            "id": function.id,
                            "name": function.name,
                            "description": function.description,
                            "ministry_id": function.ministry.id,
                            "ministry_name": function.ministry.name,
                            "created_at": function.created_at,
                        }
                        for function in user.function.all()
                    ],
                }
            )

        outbound.response = result

        return outbound
