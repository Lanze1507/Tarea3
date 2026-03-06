from django import forms
from .models import Alumno, Curso, Catedratico, AsignacionCurso, InscripcionAlumno, Nota

#clase AlumnoForm
class AlumnoForm(forms.ModelForm):
    class Meta:
        model  = Alumno
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'gender',
            'birth_date',
            'is_active',
        ]
        # id → auto, no se incluye
        # enrolled_at → auto_now_add=True, no se incluye

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Teléfono (opcional)'
            }),
            'gender': forms.Select(
                choices=[('', '-- Seleccionar --'), ('M', 'Masculino'), ('F', 'Femenino')],
                attrs={'class': 'form-select'}
            ),
            'birth_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

#clase CursoForm
class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'codigo', 'creditos']

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del curso'
            }),
            'codigo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Código del curso'
            }),
            'creditos': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Créditos'
            }),
        }
        
#clase CatedraticoForm
class CatedraticoForm(forms.ModelForm):
    class Meta:
        model = Catedratico
        fields = ['first_name', 'last_name', 'email', 'profesion']

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com'
            }),
            'profesion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Profesión'
            }),
        }

#clase AsignacionCursoForm
class AsignacionCursoForm(forms.ModelForm):
    class Meta:
        model = AsignacionCurso
        fields = ['curso', 'catedratico', 'horario']

        widgets = {
            'curso': forms.Select(attrs={
                'class': 'form-select'
            }),
            'catedratico': forms.Select(attrs={
                'class': 'form-select'
            }),
            'horario': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Lunes 7-9 AM'
            }),
        }
        
#clase InscripcionAlumnoForm
class InscripcionAlumnoForm(forms.ModelForm):
    class Meta:
        model = InscripcionAlumno
        fields = ['alumno', 'asignacion']

        widgets = {
            'alumno': forms.Select(attrs={
                'class': 'form-select'
            }),
            'asignacion': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

#clase NotaForm
class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['inscripcion', 'nota']

        widgets = {
            'inscripcion': forms.Select(attrs={
                'class': 'form-select'
            }),
            'nota': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 85.50'
            }),
        }