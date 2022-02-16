from typing import cast
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
import requests


IP_address = 'http://192.168.3.14'


class rightAPIView(APIView):
    def get(self, request: Request) -> Response:
        r = requests.get(IP_address + '/right')
        if r.status_code==200:
            return Response()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class leftAPIView(APIView):
    def get(self, request: Request) -> Response:
        r = requests.get(IP_address + '/left')
        if r.status_code==200:
            return Response()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class forwardAPIView(APIView):
    def get(self, request: Request) -> Response:
        r = requests.get(IP_address + '/forward')
        if r.status_code==200:
            return Response()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class backAPIView(APIView):
    def get(self, request: Request) -> Response:
        r = requests.get(IP_address + '/back')
        if r.status_code==200:
            return Response()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class getdataAPIView(APIView):
    def get(self, request: Request) -> Response:
        r = requests.get(IP_address + '/getdata')
        if r.status_code==200:
            return Response()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)



# Create your views here.
