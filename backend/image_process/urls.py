from django.urls import path

from . import views


urlpatterns = [
    path("image/", views.ImageGetterAPIView.as_view()),
    path("health/", views.HealthAPIView.as_view()),
    path("environment", views.EnvironmentAPIView.as_view()),
    path("start/", views.StartloopAPIView.as_view()),
    path("end/", views.EndloopAPIView.as_view()),
]
