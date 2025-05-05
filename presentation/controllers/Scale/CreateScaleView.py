from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from application.useCases.CreateScale.CreateScale import CreateScale
from application.useCases.CreateScale.protocols.CreateScaleRequest import (
    CreateScaleRequest,
)


class CreateScaleView(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request: Request) -> Response:
        required_fields = ["name", "date", "ministry_id"]

        missing_fields = [
            field for field in required_fields if not request.data.get(field)
        ]
        if missing_fields:
            return Response(
                "Missing required fields: " + ", ".join(missing_fields),
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            inbound = CreateScaleRequest()
            inbound.name = request.data.get("name")
            inbound.description = request.data.get("description")
            inbound.date = request.data.get("date")
            inbound.participants = request.data.get("participants")
            inbound.song = request.data.get("songs")
            inbound.ministry_id = request.data.get("ministry_id")

            use_case = CreateScale()
            result = use_case.execute(inbound)

            return Response(result.__dict__, status=status.HTTP_201_CREATED)

        except ObjectDoesNotExist as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)

        except IntegrityError as e:
            return Response(
                str(e),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        except ValueError as e:
            return Response(
                str(e),
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            return Response(
                str(e),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
