from django.urls import path
from .views import temp

urlpatterns = [
    path('temp', temp, name='temp'),
]
