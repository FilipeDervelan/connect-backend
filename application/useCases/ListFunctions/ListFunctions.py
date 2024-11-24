from app.models import Function
from application.useCases.ListFunctions.protocols.ListFunctionsResponse import (
    ListFunctionsResponse,
)


class ListFunctions:
    def execute(self) -> ListFunctionsResponse:
        outbound = ListFunctionsResponse()

        result = []

        functions = Function.objects.all()

        for item in functions:
            result.append(
                {
                    "id": item.id,
                    "name": item.name,
                    "description": item.description,
                    "created_at": item.created_at,
                    "ministry_id": item.ministry.id,
                    "ministry_name": item.ministry.name,
                }
            )

        outbound.response = result

        return outbound
