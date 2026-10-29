from django.shortcuts import render
from django.http import HttpResponse

def HomeView(request):
    return HttpResponse("<h1>This is the Home Page...</h1>")

