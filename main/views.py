from django.shortcuts import render
from .models import *


def home(request):
    return render(request, 'home.html')

def phase1(request):
    movie1 = Phase1.objects.all()
    return render(request, 'phase1.html', {'movie1': movie1})
def phase2(request):
    return render(request, 'phase2.html')
def phase3(request):
    return render(request, 'phase3.html')
def phase4(request):
    return render(request, 'phase4.html')
def phase5(request):
    return render(request, 'phase5.html')
def phase6(request):
    return render(request, 'phase6.html')

def info(request):
    return render(request, 'info.html')