from django.urls import path
from inicio import views

app_name = "inicio"

urlpatterns = [
    path('', views.menu, name ='Menu'),
    path("mostrar-fecha/", views.mostrar_fecha, name ="MostrarFecha"),
    path("estudiantes/", views.estudiantes, name ="Estudiantes"),
    path("Cursos/", views.cursos, name ="Cursos"),
    path("profesores/", views.profesores, name ="Profesores"),
]
