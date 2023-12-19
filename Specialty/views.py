from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from .models import speciality
# Create your views here.

def List(request):
    specialty_list = speciality.objects.all()
    specialty_json = []
    for item in specialty_list:
        specialty_json.append({
            'Specialty' : item.Name
        })
    return JsonResponse(specialty_json, safe=False)
