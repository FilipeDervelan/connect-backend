from app.models import CustomUser, Ministry
from application.useCases.ListUserMinistries.protocols.ListUserMinistriesRequest import (
    ListUserMinistriesRequest,
)
from application.useCases.ListUserMinistries.protocols.ListUserMinistriesResponse import (
    ListUserMinistriesResponse,
)


class ListUserMinistries:
    def execute(
        self,
        inbound: ListUserMinistriesRequest,
    ) -> ListUserMinistriesResponse:
        outbound = ListUserMinistriesResponse()

        user = CustomUser.objects.get(id=inbound.id)
        ministries = user.ministry.all()

        ministries_list = [
            {
                "id": ministry.id,
                "name": ministry.name,
                "description": ministry.description,
                "owner": CustomUser.objects.get(id=ministry.owner_id).username,
                "created_at": ministry.created_at,
                "updated_at": ministry.updated_at,
            }
            for ministry in ministries
        ]

        outbound.result = ministries_list

        return outbound
