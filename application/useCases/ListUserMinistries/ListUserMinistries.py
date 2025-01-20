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

        user = CustomUser.objects.filter(id=inbound.id)

        ministries = Ministry.objects.filter()

        return outbound
