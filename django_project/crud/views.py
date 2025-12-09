from django.shortcuts import render
from .forms import EstudianteForm, ProfesorForm, AsignaturaForm, CursoForm, MatriculaForm

# Vista del menú principal
def menu(request):
    return render(request, 'menu.html')

# ========================================
# VISTAS DE ESTUDIANTE
# ========================================
def estudiante_form(request):
    form = EstudianteForm()
    return render(request, 'estudiante/formEstudiante.html', {'form': form})

def estudiante_list(request):
    return render(request, 'estudiante/listEstudiante.html')

def estudiante_detail(request):
    return render(request, 'estudiante/detailEstudiante.html')

# ========================================
# VISTAS DE PROFESOR
# ========================================
def profesor_form(request):
    form = ProfesorForm()
    return render(request, 'profesor/formProfesor.html', {'form': form})

def profesor_list(request):
    return render(request, 'profesor/listProfesor.html')

def profesor_detail(request):
    return render(request, 'profesor/detailProfesor.html')

# ========================================
# VISTAS DE ASIGNATURA
# ========================================
def asignatura_form(request):
    form = AsignaturaForm()
    return render(request, 'asignatura/formAsignatura.html', {'form': form})

def asignatura_list(request):
    return render(request, 'asignatura/listAsignatura.html')

def asignatura_detail(request):
    return render(request, 'asignatura/detailAsignatura.html')

# ========================================
# VISTAS DE CURSO
# ========================================
def curso_form(request):
    form = CursoForm()
    return render(request, 'curso/formCurso.html', {'form': form})

def curso_list(request):
    return render(request, 'curso/listCurso.html')

def curso_detail(request):
    return render(request, 'curso/detailCurso.html')

# ========================================
# VISTAS DE MATRÍCULA
# ========================================
def matricula_form(request):
    form = MatriculaForm()
    return render(request, 'matricula/formMatricula.html', {'form': form})

def matricula_list(request):
    return render(request, 'matricula/listMatricula.html')

def matricula_detail(request):
    return render(request, 'matricula/detailMatricula.html')