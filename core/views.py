from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "core/inicio.html")

def sesion(request):
    return render(request, "core/sesion.html")