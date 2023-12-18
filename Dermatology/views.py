from django.http.response import JsonResponse
from django.shortcuts import render
from Speciality.models import doctor

# Create your views here.
def List(request):
    doctor_list = doctor.objects.all()
    derma_doctor_list = []
    for doci in doctor_list:
        if doci.Specialty.Name == 'Dermatology':
            derma_doctor_list.append({
                'Name' : doci.Name,
                'Speciality' : doci.Specialty.Name
            })
    return JsonResponse(request, derma_doctor_list, safe=False)




