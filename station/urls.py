from django.urls import path, include #include enables us to get the template from another app
from . import views #this enables us to interact with views.py

app_name = 'station_app'

urlpatterns = [
    path('', views.report, name="station"),
]