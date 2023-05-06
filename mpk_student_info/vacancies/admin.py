from django.contrib import admin
from .models import Student,Company,Speciality,Vacancy

admin.site.register(Student)
admin.site.register(Company)
admin.site.register(Speciality)
admin.site.register(Vacancy)