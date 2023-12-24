from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from .models import speciality, reserve
# Create your views here.
from django.shortcuts import render
from datetime import datetime
import random


def List(request):
    specialty_list = speciality.objects.all()
    specialty_json = []
    for item in specialty_list:
        specialty_json.append({
            'Specialty' : item.Name
        })
    return JsonResponse(specialty_json, safe=False)

def List_html(request):
    specialities = speciality.objects.all()
    specialities_json = {'Specialty':specialities}
    return render(request, 'Specialty/index.html', specialities_json)


def detail(request, code):
    if request.method == 'GET':
        try:
            speciality = speciality.objects.get(no=code)
        except:
            speciality = None
        f_list = {
            'speciality' : speciality, 
            'flag' : False
        }
        return render(request, 'speciality/detail.html', context=f_list)
    if request.method == 'POST':
        current_speciality = speciality.objects.get(no=code)
        email=request.POST['email']
        name=request.POST['name']
        lastname=request.POST['lastname']
        nationalid=request.POST['nationalid']
        date=request.POST['date']
        # check available seat
        # if name == '':
        #     return HttpResponse('Error: Name should not be empty')
        # if int(current_speciality.capacity) < int():
        #     return HttpResponse("Error: There is no enough seat. max seat available is :{}".format(current_flight.capacity))
        reserve.objects.create(
            speciality=current_speciality,
            name=name,
            lastname=lastname,
            email = email,
            nationalid=nationalid,
            date=date,
            reservation_code=generate_reservation_code()
        )
        # current_speciality.capacity = current_flight.capacity - int(seat)
        current_speciality.save()
        f_list = {
            'speciality' : current_speciality,
            'flag' : True
        }
        return render(request, 'Specialty/detail.html', context=f_list)
    
