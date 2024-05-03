from datetime import datetime
from app.models import Unavailability
from application.useCases.UpdateUnavailability.protocols.UpdateUnavailabilityRequest import UpdateUnavailabilityRequest
from application.useCases.UpdateUnavailability.protocols.UpdateUnavailabilityResponse import UpdateUnavailabilityResponse


class UpdateUnavailability:
    def execute(self, inbound: UpdateUnavailabilityRequest) -> UpdateUnavailabilityResponse:
        obj = Unavailability.objects.get(id=inbound.id)

        startDate = datetime.strptime(inbound.start_date, '%d/%m/%Y')
        startDate = startDate.strftime('%Y-%m-%d')

        endDate = datetime.strptime(inbound.end_date, '%d/%m/%Y')
        endDate = endDate.strftime('%Y-%m-%d')

        obj.start_date = startDate
        obj.end_date = endDate
        obj.updated_at = datetime.now()

        obj.save()

        result = UpdateUnavailabilityResponse()
        result.response = "Updated"
        result.status = 200

        return result