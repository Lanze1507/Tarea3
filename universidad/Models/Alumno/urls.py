from django.urls import path
from . import views

app_name = 'alumno'

urlpatterns = [
    path('',                     views.alumno_list,   name='list'),
    path('crear/',               views.alumno_create, name='create'),
    path('<int:pk>/',            views.alumno_detail, name='detail'),
    path('<int:pk>/editar/',     views.alumno_edit,   name='edit'),
    path('<int:pk>/eliminar/',   views.alumno_delete, name='delete'),

    path('cursos/',                      views.curso_list,   name='curso_list'),
    path('cursos/crear/',                views.curso_create, name='curso_create'),
    path('cursos/<int:pk>/',             views.curso_detail, name='curso_detail'),
    path('cursos/<int:pk>/editar/',      views.curso_edit,   name='curso_edit'),
    path('cursos/<int:pk>/eliminar/',    views.curso_delete, name='curso_delete'),

    path('catedraticos/',                   views.catedratico_list,   name='catedratico_list'),
    path('catedraticos/crear/',             views.catedratico_create, name='catedratico_create'),
    path('catedraticos/<int:pk>/',          views.catedratico_detail, name='catedratico_detail'),
    path('catedraticos/<int:pk>/editar/',   views.catedratico_edit,   name='catedratico_edit'),
    path('catedraticos/<int:pk>/eliminar/', views.catedratico_delete, name='catedratico_delete'),

    path('asignaciones/',                   views.asignacion_list,   name='asignacion_list'),
    path('asignaciones/crear/',             views.asignacion_create, name='asignacion_create'),
    path('asignaciones/<int:pk>/',          views.asignacion_detail, name='asignacion_detail'),
    path('asignaciones/<int:pk>/editar/',   views.asignacion_edit,   name='asignacion_edit'),
    path('asignaciones/<int:pk>/eliminar/', views.asignacion_delete, name='asignacion_delete'),

    path('inscripciones/',                   views.inscripcion_list,   name='inscripcion_list'),
    path('inscripciones/crear/',             views.inscripcion_create, name='inscripcion_create'),
    path('inscripciones/<int:pk>/',          views.inscripcion_detail, name='inscripcion_detail'),
    path('inscripciones/<int:pk>/editar/',   views.inscripcion_edit,   name='inscripcion_edit'),
    path('inscripciones/<int:pk>/eliminar/', views.inscripcion_delete, name='inscripcion_delete'),

    path('notas/',                   views.nota_list,   name='nota_list'),
    path('notas/crear/',             views.nota_create, name='nota_create'),
    path('notas/<int:pk>/',          views.nota_detail, name='nota_detail'),
    path('notas/<int:pk>/editar/',   views.nota_edit,   name='nota_edit'),
    path('notas/<int:pk>/eliminar/', views.nota_delete, name='nota_delete'),
    
    path('reportes/alumnos-cursos/', views.reporte_alumnos_cursos, name='reporte1'),
    path('reportes/notas/', views.reporte_notas, name='reporte2'),
]