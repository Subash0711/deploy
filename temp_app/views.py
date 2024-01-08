from django.shortcuts import render
from django.http import HttpResponse

def temp(request):
    return HttpResponse("<h1>From deploying</h1>")
