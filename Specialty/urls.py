from django.urls import path, include
from .views import List

urlpatterns = [
    path('', List),
    path('dermatology/', include('Dermatology.urls')),
    path('Pulmonology/',include('Pulmonology.urls')),
    path('Neurology/',include('Neurology.urls')),
    path('Nephrology/',include('Nephrology.urls')),
    path('Hematology/',include('Hematology.urls')),
    path('Dermatology/',include('Dermatology.urls')),
    path('Cardiology/',include('Cardiology.urls'))
]

