from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from core.models import ventasmqtt

@login_required
def home(request):
    return render(request, 'core/home.html',)

@login_required
def ventas(request):
    datos=ventasmqtt.objects.all()
    return render(request, 'core/ventas.html', {'datos':datos})

def exit(request):
    logout(request)
    return redirect('login')