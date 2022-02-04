from django.http import HttpResponse
from django.shortcuts import render

from AppCoder.forms import CursoFormulario

from .models import Curso

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
""""
Este metodo es para crear el formulario en el html
def curso_formulario(request):

    if request.method == 'POST':
        r_nombre = request.POST['curso']
        r_camada = request.POST['camada']
        curso = Curso(nombre = r_nombre, camada = r_camada) # es importante asignar los parametros porque sino salta error de id
        curso.save()        
    return render(request, 'AppCoder/curso_formulario.html')
"""

def curso_formulario(request):
    
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.data
            
            r_curso = informacion['nombre']
            r_camada = informacion['camada']
            
            curso = Curso(nombre = r_curso, camada = r_camada) # es importante asignar los parametros porque sino salta error de id
            curso.save()
    miFormulario=CursoFormulario()       #en este caso deja el formulario vacío 

    return render(request, 'AppCoder/curso_formulario.html', {"miFormulario": miFormulario})

def busquedaCamada(request):
    return render(request, 'AppCoder/busquedaCamada.html')

def buscar(request):
    
    respuesta = f"Estoy buscando la camada numero: {request.GET['camada']}"

    return HttpResponse(respuesta)