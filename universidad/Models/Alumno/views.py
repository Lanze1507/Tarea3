from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Alumno, Curso, Catedratico, AsignacionCurso, InscripcionAlumno, Nota
from .forms import AlumnoForm, CursoForm, CatedraticoForm, AsignacionCursoForm, InscripcionAlumnoForm, NotaForm

#Alumno
def alumno_list(request):
    query   = request.GET.get('q', '')
    alumnos = Alumno.objects.all()

    if query:
        alumnos = alumnos.filter(first_name__icontains=query) \
                | alumnos.filter(last_name__icontains=query)  \
                | alumnos.filter(email__icontains=query)

    return render(request, 'alumno/list.html', {
        'alumnos': alumnos,
        'query':   query
    })

def alumno_detail(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    return render(request, 'alumno/detail.html', {'alumno': alumno})

def alumno_create(request):
    form = AlumnoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Alumno registrado correctamente.')
        return redirect('alumno:list')
    return render(request, 'alumno/form.html', {
        'form':  form,
        'title': 'Nuevo Alumno'
    })

def alumno_edit(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    form   = AlumnoForm(request.POST or None, instance=alumno)
    if form.is_valid():
        form.save()
        messages.success(request, 'Alumno actualizado correctamente.')
        return redirect('alumno:list')
    return render(request, 'alumno/form.html', {
        'form':  form,
        'title': f'Editar: {alumno.first_name} {alumno.last_name}'
    })

def alumno_delete(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        alumno.delete()
        messages.success(request, 'Alumno eliminado.')
        return redirect('alumno:list')
    return render(request, 'alumno/confirm_delete.html', {'alumno': alumno})

#CURSOS
def curso_list(request):
    cursos = Curso.objects.all()
    return render(request, 'curso/list.html', {'cursos': cursos})


def curso_detail(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'curso/detail.html', {'curso': curso})


def curso_create(request):
    form = CursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Curso creado correctamente.')
        return redirect('alumno:curso_list')
    return render(request, 'curso/form.html', {
        'form': form,
        'title': 'Nuevo Curso'
    })


def curso_edit(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    form = CursoForm(request.POST or None, instance=curso)
    if form.is_valid():
        form.save()
        messages.success(request, 'Curso actualizado.')
        return redirect('alumno:curso_list')
    return render(request, 'curso/form.html', {
        'form': form,
        'title': f'Editar: {curso.nombre}'
    })


def curso_delete(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        messages.success(request, 'Curso eliminado.')
        return redirect('alumno:curso_list')
    return render(request, 'curso/confirm_delete.html', {'curso': curso})

# CATEDRATICOS

def catedratico_list(request):
    catedraticos = Catedratico.objects.all()
    return render(request, 'catedratico/list.html', {'catedraticos': catedraticos})


def catedratico_detail(request, pk):
    catedratico = get_object_or_404(Catedratico, pk=pk)
    return render(request, 'catedratico/detail.html', {'catedratico': catedratico})


def catedratico_create(request):
    form = CatedraticoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Catedrático creado correctamente.')
        return redirect('alumno:catedratico_list')
    return render(request, 'catedratico/form.html', {
        'form': form,
        'title': 'Nuevo Catedrático'
    })


def catedratico_edit(request, pk):
    catedratico = get_object_or_404(Catedratico, pk=pk)
    form = CatedraticoForm(request.POST or None, instance=catedratico)
    if form.is_valid():
        form.save()
        messages.success(request, 'Catedrático actualizado.')
        return redirect('alumno:catedratico_list')
    return render(request, 'catedratico/form.html', {
        'form': form,
        'title': f'Editar: {catedratico.first_name} {catedratico.last_name}'
    })


def catedratico_delete(request, pk):
    catedratico = get_object_or_404(Catedratico, pk=pk)
    if request.method == 'POST':
        catedratico.delete()
        messages.success(request, 'Catedrático eliminado.')
        return redirect('alumno:catedratico_list')
    return render(request, 'catedratico/confirm_delete.html', {'catedratico': catedratico})

#AsignacionCurso

def asignacion_list(request):
    asignaciones = AsignacionCurso.objects.select_related('curso', 'catedratico')
    return render(request, 'asignacion/list.html', {'asignaciones': asignaciones})


def asignacion_detail(request, pk):
    asignacion = get_object_or_404(AsignacionCurso, pk=pk)
    return render(request, 'asignacion/detail.html', {'asignacion': asignacion})


def asignacion_create(request):
    form = AsignacionCursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Asignación creada correctamente.')
        return redirect('alumno:asignacion_list')
    return render(request, 'asignacion/form.html', {
        'form': form,
        'title': 'Nueva Asignación'
    })


def asignacion_edit(request, pk):
    asignacion = get_object_or_404(AsignacionCurso, pk=pk)
    form = AsignacionCursoForm(request.POST or None, instance=asignacion)
    if form.is_valid():
        form.save()
        messages.success(request, 'Asignación actualizada.')
        return redirect('alumno:asignacion_list')
    return render(request, 'asignacion/form.html', {
        'form': form,
        'title': f'Editar Asignación'
    })


def asignacion_delete(request, pk):
    asignacion = get_object_or_404(AsignacionCurso, pk=pk)
    if request.method == 'POST':
        asignacion.delete()
        messages.success(request, 'Asignación eliminada.')
        return redirect('alumno:asignacion_list')
    return render(request, 'asignacion/confirm_delete.html', {'asignacion': asignacion})

# INSCRIPCION ALUMNO

def inscripcion_list(request):
    inscripciones = InscripcionAlumno.objects.select_related('alumno', 'asignacion')
    return render(request, 'inscripcion/list.html', {'inscripciones': inscripciones})


def inscripcion_detail(request, pk):
    inscripcion = get_object_or_404(InscripcionAlumno, pk=pk)
    return render(request, 'inscripcion/detail.html', {'inscripcion': inscripcion})


def inscripcion_create(request):
    form = InscripcionAlumnoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Inscripción creada correctamente.')
        return redirect('alumno:inscripcion_list')
    return render(request, 'inscripcion/form.html', {
        'form': form,
        'title': 'Nueva Inscripción'
    })


def inscripcion_edit(request, pk):
    inscripcion = get_object_or_404(InscripcionAlumno, pk=pk)
    form = InscripcionAlumnoForm(request.POST or None, instance=inscripcion)
    if form.is_valid():
        form.save()
        messages.success(request, 'Inscripción actualizada.')
        return redirect('alumno:inscripcion_list')
    return render(request, 'inscripcion/form.html', {
        'form': form,
        'title': 'Editar Inscripción'
    })


def inscripcion_delete(request, pk):
    inscripcion = get_object_or_404(InscripcionAlumno, pk=pk)
    if request.method == 'POST':
        inscripcion.delete()
        messages.success(request, 'Inscripción eliminada.')
        return redirect('alumno:inscripcion_list')
    return render(request, 'inscripcion/confirm_delete.html', {'inscripcion': inscripcion})

# NOTAS

def nota_list(request):
    notas = Nota.objects.select_related('inscripcion')
    return render(request, 'nota/list.html', {'notas': notas})


def nota_detail(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    return render(request, 'nota/detail.html', {'nota': nota})


def nota_create(request):
    form = NotaForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Nota registrada correctamente.')
        return redirect('alumno:nota_list')
    return render(request, 'nota/form.html', {
        'form': form,
        'title': 'Nueva Nota'
    })


def nota_edit(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    form = NotaForm(request.POST or None, instance=nota)
    if form.is_valid():
        form.save()
        messages.success(request, 'Nota actualizada.')
        return redirect('alumno:nota_list')
    return render(request, 'nota/form.html', {
        'form': form,
        'title': 'Editar Nota'
    })


def nota_delete(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    if request.method == 'POST':
        nota.delete()
        messages.success(request, 'Nota eliminada.')
        return redirect('alumno:nota_list')
    return render(request, 'nota/confirm_delete.html', {'nota': nota})

# Reportes y consultas combinadas

def reporte_alumnos_cursos(request):
    from .models import InscripcionAlumno

    data = InscripcionAlumno.objects.select_related(
        'alumno',
        'asignacion__curso'
    )

    return render(request, 'reportes/reporte1.html', {
        'data': data
    })
    
def reporte_notas(request):
    from .models import Nota

    data = Nota.objects.select_related(
        'inscripcion__alumno',
        'inscripcion__asignacion__curso'
    )

    return render(request, 'reportes/reporte2.html', {
        'data': data
    })
    
    