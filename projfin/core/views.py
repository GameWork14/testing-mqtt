from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import paho.mqtt.client as mqtt
import json
from core.models import ventasmqtt
from core.models import Alarmasmqtt
from core.models import sensor1mqtt
import json


def on_connect(client, userdata, flags, rc):
        print("Conectado: " + str(rc))

        client.subscribe("ASLW/Ventas")
        client.subscribe("ASLW/Alarmas")
        client.subscribe("ASLW/sensor1")

def on_message(client, userdata, msg):

    print(msg.topic+" "+str(msg.payload))
    payload=json.loads(msg.payload)

    if msg.topic == "ASLW/sensor1":
        sensor1mqtt.objects.create(
            sensor=payload['sensor'],
        )

    if msg.topic == "ASLW/Alarmas":
        Alarmasmqtt.objects.create(
            Alarmas=payload['alarmas'],
        )
            
    if msg.topic == "ASLW/Ventas":
        ventasmqtt.objects.create(
            cliente=payload['cliente'],
            cemento=payload['cemento'],
            arena=payload['arena'],
            grava=payload['grava'],
            aditivo=payload['aditivo'],
            placa=payload['placa'],
        )

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

client.loop_start()

@login_required
def home(request):
    return render(request, 'core/home.html',)
    
@login_required
def boton_manual(request):
    client.publish("ASLW/Actuadores", json.dumps({"Operacion" : "Manual"}))
    return render(request, 'core/home.html',)

@login_required
def boton_automatico(request):
    client.publish("ASLW/Actuadores", json.dumps({"Operacion" : "Automatico"}))
    return render(request, 'core/home.html',)

@login_required
def ventas(request):
    datos=ventasmqtt.objects.all()
    return render(request, 'core/ventas.html', {'datos':datos})

@login_required
def Alarmas(request):
    alarmas=Alarmasmqtt.objects.all()
    return render(request, 'core/Alarmas.html', {'alarmas':alarmas})

def exit(request):
    logout(request)
    return redirect('login')

from django.http import HttpResponse
import random

def sensor1(request):
    data = sensor1mqtt.objects.all().last()
    return HttpResponse(str(data.sensor))