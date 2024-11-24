from datetime import datetime


class UpdateScaleRequest:
    id: int
    name: str
    description: str
    date: datetime
    songs: list
    participants: list
