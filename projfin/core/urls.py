from django.urls import path
from .views import home, exit, ventas, Alarmas, boton_manual,boton_automatico, sensor1


urlpatterns = [
    path("", home, name="home"),
    path('logout/', exit, name='exit'),
    path("ventas/", ventas, name="ventas"),
    path("alarmas/", Alarmas, name="alarmas"),
    path("boton_manual/", boton_manual, name="boton_manual"),
    path("boton_automatico/", boton_automatico, name="boton_automatico"),
    path("sensor1/", sensor1, name="sensor1"),
]