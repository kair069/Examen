from django.urls import path
from . import views

urlpatterns = [
    path('sensordata/', views.lista_sensordata, name='lista_sensordata'),
    path('chart/', views.temperature_humidity_chart, name='temperature_humidity_chart'),
]
