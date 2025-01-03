import datetime


class UpdateUserRequest:
    id: int
    username: str
    first_name: str
    last_name: str
    birth_date: datetime
