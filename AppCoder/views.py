from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def curso(request):
    return render(request, 'AppCoder/cursos.html')

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')