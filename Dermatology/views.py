from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render
from Specialty.models import doctor
#پوست

def List(request):
    doctor_list = doctor.objects.all()
    derma_doctor_list = []
    for doci in doctor_list:
        if doci.Specialty.Name == 'Dermatology':
            derma_doctor_list.append({
                'Name' : doci.Name,
                'Speciality' : doci.Specialty.Name
            })
    return JsonResponse(derma_doctor_list, safe=False)

def List2(request):
    return HttpResponse('Hi from derma app')
