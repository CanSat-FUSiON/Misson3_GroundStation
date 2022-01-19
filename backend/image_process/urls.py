from django.urls import path

from . import views


urlpatterns = [
    path("image/", views.ImageGetterAPIView.as_view()),
]
