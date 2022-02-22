from typing import cast
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
import requests

IP_address_cam = 'http://cb11-2400-2200-76a-fa56-2954-c527-14d1-d31a.ngrok.io'
IP_address_wroom = 'http://8fe7-2400-2200-76a-fa56-2954-c527-14d1-d31a.ngrok.io'


class rightAPIView(APIView):
    def get(self, request: Request) -> Response:
        r = requests.get(IP_address_wroom + '/right')
        if r.status_code==200:
            return Response()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class leftAPIView(APIView):
    def get(self, request: Request) -> Response:
        r = requests.get(IP_address_wroom + '/left') 
        if r.status_code==200:
            return Response()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class forwardAPIView(APIView):
    def get(self, request: Request) -> Response:
        r = requests.get(IP_address_wroom + '/forward')
        if r.status_code==200:
            return Response()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class backAPIView(APIView):
    def get(self, request: Request) -> Response:
        r = requests.get(IP_address_wroom + '/back')
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
