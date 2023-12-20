from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render
from Specialty.models import doctor
#قلب
def List(request):
    doctor_list = doctor.objects.all()
    cardio_doctor_list = []
    for doci in doctor_list:
        if doci.Specialty.Name == 'Cardiology':
            cardio_doctor_list.append({
                'Name' : doci.Name,
                'Specialty' : doci.Specialty.Name
            })
    return JsonResponse(cardio_doctor_list, safe=False)





