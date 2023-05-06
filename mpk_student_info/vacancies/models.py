from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    LastName = models.CharField(verbose_name='Фамилия', max_length=150)
    Name = models.CharField(max_length=150, verbose_name='Имя')
    FatherName = models.CharField(max_length=150, verbose_name='Отчество')

    Group = models.CharField(max_length=200, verbose_name='Группа')
    PhoneNumber = models.CharField(max_length=60, verbose_name='Номер телефона')
    EndCollege = models.DateField(verbose_name='Окончание колледжа')
    Speciality = models.CharField(max_length=200, verbose_name='Специальность')
    Employment = models.CharField(max_length=500, verbose_name='Трудоустройство')
    
    User = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True, verbose_name='Пользователь')

    def __str__(self):
        return (f'{self.LastName} {self.Name} {self.FatherName}')

class Company(models.Model):
    CompanyName = models.CharField(max_length=200, verbose_name='Название компании')
    PhoneNumber = models.CharField(max_length=60, verbose_name='Номер телефона')

    def __str__(self):
        return (f'{self.CompanyName}')
       
class Speciality(models.Model):
    SpecialityName = models.CharField(max_length=300, verbose_name='Название специальности')
    
    def __str__(self):
        return (f'{self.SpecialityName}')
    
class Vacancy(models.Model):
    CreatedDate = models.DateTimeField(auto_now=True, verbose_name='Дата оздания')
    Salary = models.IntegerField(blank=True, null=True, verbose_name='Зарплата')

    Speciality = models.ForeignKey(Speciality, on_delete = models.CASCADE, verbose_name='Специальность')
    Company = models.ForeignKey(Company, on_delete = models.CASCADE, verbose_name='Компания')

    def __str__(self):
        return (f'{self.Speciality.SpecialityName}')