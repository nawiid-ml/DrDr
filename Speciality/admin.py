from django.contrib.admin import ModelAdmin, register
from .models import speciality, doctor, patient, reserve, comment

@register(speciality)
class speciality_admin(ModelAdmin):
    pass

@register(doctor)
class doctor_admin(ModelAdmin):
    pass

@register(patient)
class patient_admin(ModelAdmin):
    pass

@register(reserve)
class reserve_admin(ModelAdmin):
    pass

@register(comment)
class comment_admin(ModelAdmin):
    pass
