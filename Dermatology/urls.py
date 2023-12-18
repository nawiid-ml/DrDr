from django.urls import path
from .views import List

url_patterns = [
    path('/', List)
]