from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def green_for(request):
    return HttpResponse(f"Green For {random.randint(0, 1000)}")


def main_page(request):
    return render(request, 'main.html')


def completed_projects(request):
    return render(request, 'completed.html')
