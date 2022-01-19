from typing import cast
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import ImageTestModel
from .serializers import ImageTestSerializer


class ImageGetterAPIView(APIView):
    def post(self, request: Request) -> Response:
        serializer = ImageTestSerializer(data=request.data)
        validated_data = cast(dict, serializer.validated_data)

        ImageTestModel.objects.create(image=validated_data["image"])
        return Response(status=status.HTTP_200_OK)


class HealthAPIView(APIView):
    def get(self, request: Request) -> Response:
        return Response()
