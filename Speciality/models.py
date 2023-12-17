from django.db import models
from django.utils import timezone

class speciality(models.Model):
    Name_Specialty = models.CharField(max_length=100)



class doctor(models.Model):
    Name=models.CharField(max_length=200)
    Family=models.CharField(max_length=200)
    Specialty = models.ForeignKey('speciality', on_delete=models.CASCADE, null=True)
    Gender=models.BooleanField(help_text=" Light tick for male , Hide tick for female") # True for male , False for female
    Scores=models.FloatField(help_text="Please be between 1 and 5")
    PhoneNumber=models.CharField(max_length=13)
    Address=models.TextField()


class patient(models.Model):
    Name=models.CharField(max_length=200)
    Family=models.CharField(max_length=200)
    Age=models.PositiveIntegerField()
    PhoneNumber=models.CharField(max_length=13)
    
    



class reserve(models.Model):
    Name=models.CharField(max_length=200)
    Family=models.CharField(max_length=200)
    PhoneNumber=models.CharField(max_length=13)
    DateAndTime=models.DateTimeField(default=timezone.now)
    Name_Doctor=models.ForeignKey("doctor",on_delete=models.PROTECT)
 

    


class comment(models.Model):
    Text=models.TextField()
    PatientName=models.ForeignKey("patient",on_delete=models.PROTECT)
