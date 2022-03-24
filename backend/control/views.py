from typing import cast
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
import requests


# IP_address_wroom = "http://192.168.3.15"


def getURL(request):
    if "esp" in request.GET:
        esp32URL = request.GET.get("esp")
        return esp32URL


class rightAPIView(APIView):
    def get(self, request: Request, time) -> Response:
        r = requests.get(getURL(request) + "/right" + "?ms=" + str(time))
        if r.status_code == 200:
            return Response()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class right0APIView(APIView):
    def get(self, request: Request) -> Response:
        r = requests.get(getURL(request) + "/right")
        if r.status_code == 200:
            return Response()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class leftAPIView(APIView):
    def get(self, request: Request, time) -> Response:
        r = requests.get(getURL(request) + "/left" + "?ms=" + str(time))
        if r.status_code == 200:
            return Response()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class left0APIView(APIView):
    def get(self, request: Request) -> Response:
        r = requests.get(getURL(request) + "/left")
        if r.status_code == 200:
            return Response()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class forwardAPIView(APIView):
    def get(self, request: Request, time) -> Response:
        print(getURL(request))
        r = requests.get(getURL(request) + "/forward" + "?ms=" + str(time))
        if r.status_code == 200:
            return Response()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class forward0APIView(APIView):
    def get(self, request: Request) -> Response:
        r = requests.get(getURL(request) + "/forward")
        if r.status_code == 200:
            return Response()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class backAPIView(APIView):
    def get(self, request: Request, time) -> Response:
        r = requests.get(getURL(request) + "/back" + "?ms=" + str(time))
        if r.status_code == 200:
            return Response()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class back0APIView(APIView):
    def get(self, request: Request) -> Response:
        r = requests.get(getURL(request) + "/back")
        if r.status_code == 200:
            return Response()
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


# class gpsAPIView(APIView):
#     def get(self, request: Request, time) -> Response:
#         r = requests.get(IP_address_wroom + '/GPS' + '?ver=' + str(time))
#         if r.status_code==200:
#             return Response()
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)


# class gps0APIView(APIView):
#     def get(self, request: Request) -> Response:
#         r = requests.get(IP_address_wroom + '/GPS')
#         if r.status_code==200:
#             return Response()
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)


# class fireAPIView(APIView):
#     def get(self, request: Request, time) -> Response:
#         r = requests.get(IP_address_wroom + "/fire")
#         if r.status_code == 200:
#             return Response()
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)


# class fire0APIView(APIView):
#     def get(self, request: Request) -> Response:
#         r = requests.get(IP_address_wroom + "/fire")
#         if r.status_code == 200:
#             return Response()
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)


# class getdataAPIView(APIView):
#     def get(self, request: Request) -> Response:
#         r = requests.get(IP_address_wroom + "/getdata")
#         if r.status_code == 200:
#             return Response()
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)


# Create your views here.
