from datetime import datetime
from typing import List, TypedDict


class Song(TypedDict):
    id: int
    name: str


class Participant(TypedDict):
    id: int
    name: str


class Ministry(TypedDict):
    id: int
    name: str


class Scale(TypedDict):
    id: int
    name: str
    description: str
    date: datetime
    song: List[Song]
    participant: List[Participant]
    ministry: Ministry
    created_by: str
    created_at: datetime
    updated_at: datetime


class GetScaleResponse:
    result: Scale
