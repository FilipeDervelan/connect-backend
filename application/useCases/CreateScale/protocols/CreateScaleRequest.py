from datetime import datetime
from typing import List


class CreateScaleRequest:
    name: str
    description: str
    date: datetime
    song: List[int]
    participants: list
    ministry_id: int
    function: list
