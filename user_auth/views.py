from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse('<center><h1>Welcome to User Flow APIS :)</h1></center>')
