from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def on_connect(self, client, userdata, flags, rc):
        print("Conectado: " + str(rc))

        client.subscribe("ASLW/#")

    def on_message(self, client, userdata, msg):
        import json
        from core.models import ventasmqtt
        print(msg.topic+" "+str(msg.payload))
        payload=json.loads(msg.payload)
        ventasmqtt.objects.create(
            cliente=payload['cliente'],
            cemento=payload['cemento'],
            arena=payload['arena'],
            grava=payload['grava'],
            aditivo=payload['aditivo'],
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