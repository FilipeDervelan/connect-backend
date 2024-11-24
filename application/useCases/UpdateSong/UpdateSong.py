from app.models import Singer, Song
from application.useCases.UpdateSong.protocols.UpdateSongRequest import (
    UpdateSongRequest,
)
from application.useCases.UpdateSong.protocols.UpdateSongResponse import (
    UpdateSongResponse,
)


class UpdateSong:
    def execute(self, inbound: UpdateSongRequest) -> UpdateSongResponse:
        outbound = UpdateSongResponse()
        outbound.response = "Song updated"
        outbound.status = 200

        name = inbound.name
        singer_id = inbound.singer_id or None

        if not name.strip():
            outbound.response = "Name is required"
            outbound.status = 400
            return outbound

        song = Song.objects.get(id=inbound.id)

        if singer_id:
            singer = Singer.objects.get(id=singer_id)
            song.singer = singer

        song.name = name
        song.description = inbound.description
        song.link = inbound.link
        song.save()

        return outbound
