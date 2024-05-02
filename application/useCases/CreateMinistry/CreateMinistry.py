from app.models import Ministry
from application.useCases.CreateMinistry.protocols.CreateMinistryResponse import CreateMinistryResponse


class CreateMinistry:
    def execute(self, inbound):
        result = CreateMinistryResponse()

        # Verifying if required params exists
        if not inbound.name:
            result.response = "Name is required"
            result.status = 400

            return result

        # Transfering the inbound properties value to variables
        name = inbound.name
        description = inbound.description

        # Creating user
        newMinistry = Ministry(name=name, description=description)

        newMinistry.save()

        result.response = "Successfully Created"
        result.status = 201

        return result