from app.models import Song
from application.useCases.CreateSong.protocols.CreateSongRequest import (
    CreateSongRequest,
)
from application.useCases.CreateSong.protocols.CreateSongResponse import (
    CreateSongResponse,
)


class CreateSong:
    def execute(self, inbound: CreateSongRequest) -> CreateSongResponse:
        outbound = CreateSongResponse()
        outbound.response = "Song created"
        outbound.status = 201

        new_song = Song(
            name=inbound.name,
            description=inbound.description,
            link=inbound.link,
            singer=inbound.singer,
        )

        new_song.save()

        return outbound
