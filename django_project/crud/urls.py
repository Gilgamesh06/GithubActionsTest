from django.urls import path
from . import views

app_name = 'crud'

urlpatterns = [
    # Menú principal
    path('menu/', views.menu, name='menu'),
    
    # Rutas de Estudiante
    path('estudiante/', views.estudiante_form, name='estudiante_form'),
    path('estudiante/list/', views.estudiante_list, name='estudiante_list'),
    path('estudiante/detail/', views.estudiante_detail, name='estudiante_detail'),
    
    # Rutas de Profesor
    path('profesor/', views.profesor_form, name='profesor_form'),
    path('profesor/list/', views.profesor_list, name='profesor_list'),
    path('profesor/detail/', views.profesor_detail, name='profesor_detail'),
    
    # Rutas de Asignatura
    path('asignatura/', views.asignatura_form, name='asignatura_form'),
    path('asignatura/list/', views.asignatura_list, name='asignatura_list'),
    path('asignatura/detail/', views.asignatura_detail, name='asignatura_detail'),
    
    # Rutas de Curso
    path('curso/', views.curso_form, name='curso_form'),
    path('curso/list/', views.curso_list, name='curso_list'),
    path('curso/detail/', views.curso_detail, name='curso_detail'),
    
    # Rutas de Matrícula
    path('matricula/', views.matricula_form, name='matricula_form'),
    path('matricula/list/', views.matricula_list, name='matricula_list'),
    path('matricula/detail/', views.matricula_detail, name='matricula_detail'),
]
