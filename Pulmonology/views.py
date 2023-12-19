from django.http.response import JsonResponse
from django.shortcuts import render
from Specialty.models import doctor
#ریه
def List(request):
    doctor_list = doctor.objects.all()
    pulmono_doctor_list = []
    for doci in doctor_list:
        if doci.Specialty.Name == 'Pulmonology':
            pulmono_doctor_list.append({
                'Name' : doci.Name,
                'Specialty' : doci.Specialty.Name
            })
    return JsonResponse(request, pulmono_doctor_list, safe=False)




