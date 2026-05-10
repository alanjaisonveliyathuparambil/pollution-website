from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def air(request):
    return render(request, 'air.html')

def water(request):
    return render(request, 'water.html')

def noise(request):
    return render(request, 'noise.html')

def soil(request):
    return render(request, 'soil.html')

def quiz_intro(request):
    return render(request, 'quiz_intro.html')

def quiz(request):
    return render(request, 'quiz.html')