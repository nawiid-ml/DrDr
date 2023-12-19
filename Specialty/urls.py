from django.urls import path, include
from .views import List

urlpatterns = [
    path('', List),
    path('dermatology/', include('Dermatology.urls')),
]
