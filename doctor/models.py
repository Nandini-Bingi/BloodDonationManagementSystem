from django.db import models

# Create your models here.


class Doctor(models.Model):

    full_name = models.CharField(max_length=100)

    doctor_id = models.CharField(
        max_length=20,
        unique=True
    )

    password = models.CharField(
        max_length=128
    )

    hospital_name = models.CharField(
        max_length=150
    )

    def __str__(self):
        return self.full_name