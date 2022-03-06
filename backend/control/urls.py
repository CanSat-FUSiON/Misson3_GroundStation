from django.urls import path

from . import views


urlpatterns = [
    path("right/<int:time>/", views.rightAPIView.as_view(), name="right"),  # 右回り
    path("right//", views.right0APIView.as_view(), name="right0"),
    path("left/<int:time>/", views.leftAPIView.as_view(), name="left"),  # 左回り
    path("left//", views.left0APIView.as_view(), name="left0"),
    path("forward/<int:time>/", views.forwardAPIView.as_view(), name="forward"),  # 前進
    path("forward//", views.forward0APIView.as_view(), name="forward0"),
    path("back/<int:time>/", views.backAPIView.as_view(), name="back"),  # 後退
    path("back//", views.back0APIView.as_view(), name="back0"),
    # path("gps/<int:time>/", views.gpsAPIView.as_view(), name="gps"),
    # path("gps//", views.gps0APIView.as_view(), name="gps0"),
    path("fire/<int:time>/", views.fireAPIView.as_view(), name='fire'),  # ニクロム線点火
    path("fire//", views.fire0APIView.as_view(), name='fire0'),
    path("getdata/", views.getdataAPIView.as_view(), name="getdata"),
]