from django.core.management.base import BaseCommand
from universidad.Models.Alumno.models import Alumno
import random


class Command(BaseCommand):
    help = 'Poblar la base de datos con 10K alumnos'

    def handle(self, *args, **kwargs):

        for i in range(10000):
            Alumno.objects.create(
                first_name=f"Alumno{i}",
                last_name=f"Test{i}",
                email=f"alumno{i}@mail.com",
                phone="12345678",
                gender=random.choice(['M', 'F']),
                birth_date="2000-01-01",
                is_active=True
            )

        self.stdout.write(self.style.SUCCESS('10,000 alumnos creados correctamente'))