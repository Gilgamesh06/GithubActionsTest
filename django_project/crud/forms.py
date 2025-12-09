from django import forms

class EstudianteForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'id': 'nombre', 'name': 'nombre'})
    )
    apellido = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'id': 'apellido', 'name': 'apellido'})
    )
    edad = forms.IntegerField(
        widget=forms.NumberInput(attrs={'id': 'edad', 'name': 'edad'})
    )
    genero = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'id': 'genero', 'name': 'genero'})
    )

class ProfesorForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'id': 'nombre', 'name': 'nombre'})
    )
    apellido = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'id': 'apellido', 'name': 'apellido'})
    )
    edad = forms.IntegerField(
        widget=forms.NumberInput(attrs={'id': 'edad', 'name': 'edad'})
    )
    genero = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'id': 'genero', 'name': 'genero'})
    )

class AsignaturaForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'id': 'nombre', 'name': 'nombre'})
    )
    creditos = forms.IntegerField(
        widget=forms.NumberInput(attrs={'id': 'creditos', 'name': 'creditos'})
    )

class CursoForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'id': 'nombre', 'name': 'nombre'})
    )
    fid_asignatura = forms.IntegerField(
        widget=forms.NumberInput(attrs={'id': 'fid_asignatura', 'name': 'fid_asignatura'})
    )
    fid_profesor = forms.IntegerField(
        widget=forms.NumberInput(attrs={'id': 'fid_profesor', 'name': 'fid_profesor'})
    )

class MatriculaForm(forms.Form):
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={'id': 'fecha', 'name': 'fecha'})
    )
    fid_estudiante = forms.IntegerField(
        widget=forms.NumberInput(attrs={'id': 'fid_estudiante', 'name': 'fid_estudiante'})
    )
    fid_curso = forms.IntegerField(
        widget=forms.NumberInput(attrs={'id': 'fid_curso', 'name': 'fid_curso'})
    )
    

    