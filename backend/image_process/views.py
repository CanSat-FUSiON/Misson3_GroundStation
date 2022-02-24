from typing import cast
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
import requests
from django.core.files.base import ContentFile
import cv2
import numpy as np
import multiprocessing

from .models import ImageTestModel
from .serializers import ImageTestSerializer, EnvironmentSerializer
from .image_cv2.red_detect_lib import main


IP_address_cam = 'http://192.168.3.13'
IP_address_wroom = 'http://192.168.3.15'


class ImageGetterAPIView(APIView):
    def get(self, request: Request) -> Response:
        print ("Hello")
        r = requests.get(IP_address_cam + '/capture')
        img_data = r.content  # バイト列に変換
        
        img_array = cv2.imdecode(np.array(bytearray(r.content), dtype=np.uint8), -1)

        control_data = main(sampleimage=img_array)
        
        ang = round(control_data[0])
        occ = control_data[1]
        
        if occ<=0.3:
            r_2 = requests.get(IP_address_wroom + '/image_automatic' + '?a=' + str(ang))
        
        return Response()



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




def loop():
    
    judgment = 0
    
    occ = 0.003
    
    while judgment == 0:
        while 0.002 < occ:
            print('find!')
            r = requests.get(IP_address_cam + '/capture')

            img_array = cv2.imdecode(np.array(bytearray(r.content), dtype=np.uint8), -1)  # cv2で読める形に変換

            control_data = main(sampleimage=img_array)  # 占有率と角度の計算

            ang = round(control_data[0])  # 扱いやすくするために整数に変換
            occ = control_data[1]
            
            if occ > 0.3:
                print('goal!!')
                judgment = 1
            
            else:
                r_2 = requests.get(IP_address_wroom + '/image_automatic' + '?a=' + str(ang))
        
        else:
            while occ < 0.002:
                print('cannot find...')
                r_3 = requests.get(IP_address_wroom + '/right_little')
                r_4 = requests.get(IP_address_cam + '/capture')
                img_array_2 = cv2.imdecode(np.array(bytearray(r_4.content), dtype=np.uint8), -1)  # cv2で読める形に変換
                control_data_2 = main(sampleimage=img_array_2)  # 占有率と角度の計算
                occ = control_data_2[1]

        


t = multiprocessing.Process(target = loop)  # グローバルな値として定義


class StartloopAPIView(APIView):
    def get(self, request: Request) -> Response:
        
        t = multiprocessing.Process(target = loop)
        t.start()
        
        return Response()
        

class EndloopAPIView(APIView):
    def get(self, request: Request) -> Response:
        
        t.terminate()

        return Response()
    
    


    