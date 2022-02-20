from typing import cast
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
import requests

IP_address_cam = 'http://d771-60-74-77-131.ngrok.io'
IP_address_wroom = 'https://20b0-60-74-77-131.ngrok.io'


class rightAPIView(APIView):
    def get(self, request: Request) -> Response:
        r = requests.get(IP_address_wroom + '/right')
        q = requests.get(IP_address_cam + '/capture')  # htmlに画像を表示させる方法教わる
        if r.status_code==200:
            return Response()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class leftAPIView(APIView):
    def get(self, request: Request) -> Response:
        r = requests.get(IP_address_wroom + '/left')
        q = requests.get(IP_address_cam + '/capture')
        if r.status_code==200:
            return Response()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class forwardAPIView(APIView):
    def get(self, request: Request) -> Response:
        r = requests.get(IP_address_wroom + '/forward')
        q = requests.get(IP_address_cam + '/capture')
        if r.status_code==200:
            return Response()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class backAPIView(APIView):
    def get(self, request: Request) -> Response:
        r = requests.get(IP_address_wroom + '/back')
        q = requests.get(IP_address_cam + '/capture')
        if r.status_code==200:
            return Response()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class getdataAPIView(APIView):
    def get(self, request: Request) -> Response:
        r = requests.get(IP_address_wroom + '/getdata')
        if r.status_code==200:
            return Response()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)



# Create your views here.
