from typing import cast
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
import requests

from .models import ImageTestModel
from .serializers import ImageTestSerializer, EnvironmentSerializer


class ImageGetterAPIView(APIView):
    def post(self, request: Request) -> Response:
        serializer = ImageTestSerializer(data=request.data)
        validated_data = cast(dict, serializer.validated_data)

        ImageTestModel.objects.create(image=validated_data["image"])
        return Response(status=status.HTTP_200_OK)


class HealthAPIView(APIView):
    def get(self, request: Request) -> Response:
        return Response()


class ControllerForwardAPIView(APIView):
    def post(self, request: Request) -> Response:

        res = requests.post("/controller/forward")  # esp-camに対して

        return Response(status=status.HTTP_200_OK)


class EnvironmentAPIView(APIView):
    def get(self, request: Request) -> Response:

        # requestを送る
        res = requests.get("/environment")

        # 正当か判断
        serializer = EnvironmentSerializer(data=res.text)

        if serializer.is_valid():
            return Response(data=serializer.validated_data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)
