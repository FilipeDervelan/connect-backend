from app.models import Song
from application.useCases.ListSongs.protocols.ListSongsResponse import ListSongsResponse


class ListSongs:
    def execute(self) -> ListSongsResponse:
        outbound = ListSongsResponse()
        outbound.status = 200

        songs = Song.objects.all()

        result = []

        for song in songs:
            result.append(
                {
                    "name": song.name,
                    "description": song.description,
                    "link": song.link,
                    "singer_id": song.singer.id if song.singer else None,
                    "singer_name": song.singer.name if song.singer else None,
                    "created_at": song.created_at,
                }
            )

        outbound.response = result

        return outbound
