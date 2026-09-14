from django.shortcuts import render


def inicio(request):
    return render(request, 'app2/inicio.html')


def contacto(request):
    return render(request, 'app2/contacto.html')