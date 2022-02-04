from unicodedata import name
from xml.etree.ElementInclude import include
from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('cursos', views.curso, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('entregables', views.entregables, name="Entregables"),
    path('cursoformulario/', views.curso_formulario, name="AppCoderCursoFormulario"),
    path('busquedacamada/', views.busquedaCamada, name="BusquedaCamada"),
    path('buscar/', views.buscar, name="Buscar" )
]
