from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def on_connect(self, client, userdata, flags, rc):
        print("Conectado: " + str(rc))

        client.subscribe("ASLW/Ventas")
        client.subscribe("ASLW/Alarmas/Presencia")
        client.subscribe("ASLW/Alarmas/Paro")
        client.subscribe("ASLW/Alarmas/ViolacionDeActuadores")

    def on_message(self, client, userdata, msg):
        import json
        from core.models import ventasmqtt
        from core.models import Alarmasmqtt
        print(msg.topic+" "+str(msg.payload))
        payload=json.loads(msg.payload)
        if msg.topic == "ASLW/Alarmas/Presencia":
            Alarmasmqtt.objects.create(
                Presencia=payload['presencia'],
            )

        if msg.topic == "ASLW/Alarmas/Paro":
            Alarmasmqtt.objects.create(
                ParoDeEmergencia=payload['paro'],
            )

        if msg.topic == "ASLW/Alarmas/ViolacionDeActuadores":
            Alarmasmqtt.objects.create(
               ViolacionActuador =payload['ViolacionActuador'],
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


    def ready(self):
        import paho.mqtt.client as mqtt

        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message

        client.connect("test.mosquitto.org", 1883, 60)

        client.loop_start()

    def stop(self):
        self.client.loop_stop()