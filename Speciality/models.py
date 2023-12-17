from django.db import models
from django.utils import timezone

class speciality(models.Model):
    Name = models.CharField(max_length=100)

class doctor(models.Model):
    Name=models.CharField(max_length=200)
    Specialty = models.ForeignKey(speciality, on_delete=models.CASCADE)
    Sum_Scores=models.FloatField(default=0, null=True)
    Count_Scores=models.FloatField(default=0, null=True)

class patient(models.Model):
    Name=models.CharField(max_length=200)
    Age=models.PositiveIntegerField()

class reserve(models.Model):
    bimar = models.ForeignKey(patient, on_delete=models.CASCADE)
    docti = models.ForeignKey(doctor, on_delete=models.CASCADE)
    time = models.DateTimeField()

class comment(models.Model):
    user = models.CharField()
    comment = models.TextField()
    doctor = models.ForeignKey(doctor, on_delete=models.CASCADE)
