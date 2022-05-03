from django.db import models


class Doctors(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)

