from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from app.models import Scale
from application.useCases.GetScale.GetScale import GetScale
from application.useCases.GetScale.protocols.GetScaleRequest import GetScaleRequest


class GetScaleView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        try:
            if not id or not isinstance(id, int):
                return Response(
                    "Scale ID is required",
                    status.HTTP_400_BAD_REQUEST,
                )

            inbound = GetScaleRequest()
            inbound.id = id

            use_case = GetScale()
            result = use_case.execute()

            outbound = result.__dict__

            return Response(outbound)

        except Scale.DoesNotExist:
            return Response("Scale does not exist", status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)
