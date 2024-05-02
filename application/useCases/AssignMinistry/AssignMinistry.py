from app.models import Ministry, User
from application.useCases.AssignMinistry.protocols.AssignMinistryRequest import AssignMinistryRequest
from application.useCases.AssignMinistry.protocols.AssignMinistryResponse import AssignMinistryResponse


class AssignMinistry:
    def execute(self, inbound: AssignMinistryRequest) -> AssignMinistryResponse:
        user = User.objects.get(id=inbound.user_id)
        ministry = Ministry.objects.get(id=inbound.ministry_id)

        result = AssignMinistryResponse()

        user.ministry.add(ministry)

        result.response = "Ministry assigned"
        result.status = 200

        return result
