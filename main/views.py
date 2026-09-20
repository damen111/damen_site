from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def phase1(request):
    return render(request, 'phase1.html')
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