from datetime import datetime


class CreateUnavailabilityRequest:
    start_date:datetime
    end_date:datetime
    user_id:int