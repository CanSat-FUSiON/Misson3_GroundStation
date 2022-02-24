from django.urls import path

from . import views


urlpatterns = [
    path("right/", views.rightAPIView.as_view(), name="right"),  # 右回り
    path("left/", views.leftAPIView.as_view(), name="left"),  # 左回り
    path("forward/", views.forwardAPIView.as_view(), name="forward"),  # 前進
    path("back/", views.backAPIView.as_view(), name="back"),  # 後退
    path("gps/", views.gpsAPIView.as_view(), name="gps"),
    path("getdata/", views.getdataAPIView.as_view(), name="getdata"),
]