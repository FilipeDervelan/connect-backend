from app.models import Singer
from application.useCases.CreateSinger.protocols.CreateSingerRequest import (
    CreateSingerRequest,
)
from application.useCases.CreateSinger.protocols.CreateSingerResponse import (
    CreateSingerResponse,
)


class CreateSinger:
    def execute(self, inbound: CreateSingerRequest) -> CreateSingerResponse:
        outbound = CreateSingerResponse()
        outbound.response = "Singer created"
        outbound.status = 201

        name = inbound.name

        if not name.strip():
            outbound.response = "Name is required"
            outbound.status = 400
            return outbound

        new_singer = Singer(name=name)
        new_singer.save()

        return outbound
