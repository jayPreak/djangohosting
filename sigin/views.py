from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signedin(request):
    return render(request, 'signedin.html')

def kms(request):
    return render(request, 'kms.html')