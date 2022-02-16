from typing import cast
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
import requests

from .models import ImageTestModel
from .serializers import ImageTestSerializer, EnvironmentSerializer
from .image_cv2.red_detect_lib import main


IP_address_cam = '*******'
IP_address_wroom = '*******'


class ImageGetterAPIView(APIView):
    def post(self, request: Request) -> Response:
        r = requests.get(IP_address_cam + '/capture')
        serializer = ImageTestSerializer(data=r.data)
        validated_data = cast(dict, serializer.validated_data)
        ImageTestModel.objects.create(image=validated_data["image"])
        
        control_data = main(sampleimage=validated_data["image"])  # 本田チェック(validated_dataは撮れた画像のつもりです・・・)
        
        q = ImageTestModel(Rotation = control_data[0], Occupancy = control_data[1])
        q.save()
        
        return Response()
        
    def get(self, request: Request) -> Response:  # 本田チェック
        latest_data = ImageTestModel.objects.latest("created_on")
        
        ang = latest_data.Rotation
        occ = latest_data.Occupancy
        
        if occ<=0.3:
            r = requests.get(IP_address_wroom + '/image_automatic' + '?a=' + ang)  # 本田チェック
        else:
            return Response()
        
        if r.status_code==200:
            return Response()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)



class HealthAPIView(APIView):
    def get(self, request: Request) -> Response:
        return Response()



class EnvironmentAPIView(APIView):
    def get(self, request: Request) -> Response:

        # requestを送る
        res = requests.get("/environment")

        # 正当か判断
        serializer = EnvironmentSerializer(data=res.text)

        if serializer.is_valid():
            return Response(data=serializer.validated_data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)
