from django.urls import path, include
from .views import List

urlpatterns = [
    path('', List),
    path('dermatology/', include('Dermatology.urls')),
    path('pulmonology/',include('Pulmonology.urls')),
    path('neurology/',include('Neurology.urls')),
    path('nephrology/',include('Nephrology.urls')),
    path('hematology/',include('Hematology.urls')),
    path('cardiology/',include('Cardiology.urls'))
]