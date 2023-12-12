from django.contrib import admin
from .models import ventasmqtt, Alarmasmqtt

# Register your models here.
admin.site.register(ventasmqtt)
admin.site.register(Alarmasmqtt)