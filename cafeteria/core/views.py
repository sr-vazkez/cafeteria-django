from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("Inicio")


def about(request):
    return HttpResponse("historia")


def services(request):
    return HttpResponse("servicios")


def store(request):
    return HttpResponse("visitanos")


def contact(request):
    return HttpResponse("contacto")


def blog(request):
    return HttpResponse("blog")


def sample(request):
    return HttpResponse("sample")
