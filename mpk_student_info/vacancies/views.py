from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request, 'vacancies/index.html')

def Vacancies(request):
    return render(request, 'vacancies/vacancies.html')