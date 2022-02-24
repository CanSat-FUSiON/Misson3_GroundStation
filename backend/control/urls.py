from django.urls import path

from . import views


urlpatterns = [
    path("right/<int:time>/", views.rightAPIView.as_view(), name="right"),  # 右回り
    path("left/<int:time>/", views.leftAPIView.as_view(), name="left"),  # 左回り
    path("forward/<int:time>/", views.forwardAPIView.as_view(), name="forward"),  # 前進
    path("back/<int:time>/", views.backAPIView.as_view(), name="back"),  # 後退
    path("gps/", views.gpsAPIView.as_view(), name="gps"),
    path("getdata/", views.getdataAPIView.as_view(), name="getdata"),
]