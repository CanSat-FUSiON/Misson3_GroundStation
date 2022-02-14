from django.urls import path

from . import views


urlpatterns = [
    path("right/", views.rightAPIView.as_view(), name="right"),
    path("left/", views.leftAPIView.as_view(), name="left"),
    path("forward/", views.forwardAPIView.as_view(), name="forward"),
    path("back/", views.backAPIView.as_view(), name="back"),
]
