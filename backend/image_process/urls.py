from django.urls import path

from . import views


urlpatterns = [
    path("image/", views.ImageGetterAPIView.as_view()),
    path("health/", views.HealthAPIView.as_view()),
]
