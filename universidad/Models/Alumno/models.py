from django.db import models
#Alumno
class Alumno(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=1)
    birth_date = models.DateField()
    enrolled_at = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'alumno'

#Curso
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    creditos = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'curso'

#Catedratico
class Catedratico(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    profesion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'catedratico'

#AsignacionCurso
class AsignacionCurso(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    catedratico = models.ForeignKey(Catedratico, on_delete=models.CASCADE)
    horario = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.curso} - {self.catedratico}"

    class Meta:
        db_table = 'asignacion_curso'

#InscripcionAlumno
class InscripcionAlumno(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    asignacion = models.ForeignKey(AsignacionCurso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.alumno} - {self.asignacion}"

    class Meta:
        db_table = 'inscripcion_alumno'

#Nota
class Nota(models.Model):
    inscripcion = models.ForeignKey(InscripcionAlumno, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.inscripcion} - {self.nota}"

    class Meta:
        db_table = 'nota'