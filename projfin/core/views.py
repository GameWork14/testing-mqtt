from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from core.models import ventasmqtt
import paho.mqtt.client as mqtt

def enviar_mensaje_mqtt(data):
    # Configura la conexión MQTT
    client = mqtt.Client()
    client.connect("test.mosquitto.org", 1883, 60)

    # Conéctate al broker MQTT
    client.loop_start()  # Inicia el bucle MQTT en un hilo

    # Publica el mensaje en el tema deseado
    client.publish("ASLW/ModoOperacion", data)

    # Espera un poco para asegurarse de que el mensaje se envíe
    client.loop_stop()
    client.disconnect()

@login_required
def home(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        enviar_mensaje_mqtt(data)
        print(data)

    return render(request, 'core/home.html',)

@login_required
def ventas(request):
    datos=ventasmqtt.objects.all()
    return render(request, 'core/ventas.html', {'datos':datos})

def exit(request):
    logout(request)
    return redirect('login')