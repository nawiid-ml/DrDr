from django.http.response import JsonResponse
from django.shortcuts import render
from Specialty.models import doctor
#مغز
def List(request):
    doctor_list = doctor.objects.all()
    neuro_doctor_list = []
    for doci in doctor_list:
        if doci.Specialty.Name == 'Neurology':
            neuro_doctor_list.append({
                'Name' : doci.Name,
                'Specialty' : doci.Specialty.Name
            })
    return JsonResponse(neuro_doctor_list, safe=False)

def List_html(request):
    doctors = doctor.objects.all()
    doctors_list = []
    for item in doctors:
        print(item.Specialty.Name)
        if item.Specialty.Name == 'Neurology':
            print('Found')
            doctors_list.append(item)
    doctors_json = {'Doctor' : doctors_list}
    return render(request, 'Logy/logy.html', doctors_json)


