from django.shortcuts import render
from .models import Vacancy

# Create your views here.

def Index(request):
    return render(request, 'vacancies/index.html')

def Vacancies(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancies/vacancies.html', {'vacancies':vacancies})