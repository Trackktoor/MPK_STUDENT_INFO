from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    LastName = models.CharField(150)
    Name = models.CharField(150)
    FatherName = models.CharField(150)

    Group = models.CharField(200)
    PhoneNumber = models.CharField(60)
    EndCollege = models.DateField()
    Speciality = models.CharField(200)
    Employment = models.CharField(500)
    
    User = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)

class Company(models.Model):
    CompanyName = models.CharField(200)
    PhoneNumber = models.CharField(60)

class Speciality(models.Model):
    SpecialityName = models.CharField(300)

class Vacancy(models.Model):
    CreatedDate = models.DateTimeField(auto_now=True)
    Salary = models.IntegerField(blank=True, null=True)

    Speciality = models.ForeignKey(Speciality, on_delete = models.CASCADE)
    Company = models.ForeignKey(Company, on_delete = models.CASCADE)