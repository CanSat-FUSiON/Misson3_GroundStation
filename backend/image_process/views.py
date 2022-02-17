from typing import cast
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
import requests
from django.core.files.base import ContentFile

from .models import ImageTestModel
from .serializers import ImageTestSerializer, EnvironmentSerializer
from .image_cv2.red_detect_lib import main


IP_address_cam = '*******'
IP_address_wroom = '*******'


class ImageGetterAPIView(APIView):
    def post(self, request: Request) -> Response:
        r = requests.get(IP_address_cam + '/capture')
        image = ContentFile(r.content)  # データがCV2で読める形にする
        
        control_data = main(sampleimage=image)
        
        #q = ImageTestModel(Rotation = control_data[0], Occupancy = control_data[1])
        
        ang = control_data[0]
        occ = control_data[1]
        
        if occ<=0.3:
            r_2 = request.get(IP_address_wroom + '/image_automatic' + '?a=' + ang)
        
        return Response()
        
    def get(self, request: Request) -> Response:  # 本田チェック
        r = requests.get(IP_address_cam + '/capture')
        image = ContentFile(r.content)  # データがCV2で読める形にする
        
        control_data = main(sampleimage=image)
        
        q = ImageTestModel(Rotation = control_data[0], Occupancy = control_data[1])
        q.save()
        
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
