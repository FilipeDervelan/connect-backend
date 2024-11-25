from app.models import Ministry
from application.useCases.CreateMinistry.protocols.CreateMinistryRequest import (
    CreateMinistryRequest,
)
from application.useCases.CreateMinistry.protocols.CreateMinistryResponse import (
    CreateMinistryResponse,
)


class CreateMinistry:
    def execute(
        self,
        inbound: CreateMinistryRequest,
    ) -> CreateMinistryResponse:
        result = CreateMinistryResponse()

        if not inbound.name:
            result.response = "Name is required"
            result.status = 400

            return result

        name = inbound.name
        description = inbound.description if inbound.description else None

        ministry = Ministry.objects.filter(name=name)

        if ministry.exists():
            result.response = "Ministry already exists"
            result.status = 400

            return result

        new_ministry = Ministry(
            name=name,
            description=description,
            owner_id=inbound.user_id,
        )

        new_ministry.save()

        result.response = "Successfully Created"
        result.status = 201

        return result
