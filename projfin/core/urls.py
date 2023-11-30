from django.urls import path
from .views import home, exit, ventas


urlpatterns = [
    path("", home, name="home"),
    path('logout/', exit, name='exit'),
    path("ventas/", ventas, name="ventas")
]