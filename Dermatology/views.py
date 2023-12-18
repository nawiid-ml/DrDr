from django.shortcuts import render
from Speciality.models import doctor

# Create your views here.
def List():
    doctor_list = doctor.objects.all()
    for doci in doctor_list:
        if doci.Specialty



