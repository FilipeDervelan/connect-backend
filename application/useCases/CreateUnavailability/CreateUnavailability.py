from datetime import datetime
from app.models import Unavailability, User
from application.useCases.CreateUnavailability.protocols.CreateUnavailabilityRequest import CreateUnavailabilityRequest
from application.useCases.CreateUnavailability.protocols.CreateUnavailabilityResponse import CreateUnavailabilityResponse


class CreateUnavailability:
    def execute(self, inbound: CreateUnavailabilityRequest) -> CreateUnavailabilityResponse:
        user = User.objects.get(id=inbound.user_id)

        startDate = datetime.strptime(inbound.start_date, '%d/%m/%Y')
        startDate = startDate.strftime('%Y-%m-%d')

        endDate = datetime.strptime(inbound.end_date, '%d/%m/%Y')
        endDate = endDate.strftime('%Y-%m-%d')

        newUnavailability = Unavailability(start_date=startDate, end_date=endDate, user=user)

        newUnavailability.save()

        result = CreateUnavailabilityResponse()
        result.response = "Successfully created"
        result.status = 201

        return result