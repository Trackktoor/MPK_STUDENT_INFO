# Generated by Django 4.2.1 on 2023-05-06 17:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompanyName', models.CharField(verbose_name=200)),
                ('PhoneNumber', models.CharField(verbose_name=60)),
            ],
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SpecialityName', models.CharField(verbose_name=300)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('LastName', models.CharField(verbose_name=150)),
                ('Name', models.CharField(verbose_name=150)),
                ('FatherName', models.CharField(verbose_name=150)),
                ('Group', models.CharField(verbose_name=200)),
                ('PhoneNumber', models.CharField(verbose_name=60)),
                ('EndCollege', models.DateField()),
                ('Speciality', models.CharField(verbose_name=200)),
                ('Employment', models.CharField(verbose_name=500)),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreatedDate', models.DateTimeField(auto_now=True)),
                ('Salary', models.IntegerField(blank=True, null=True)),
                ('Company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancies.company')),
                ('Speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancies.speciality')),
            ],
        ),
    ]
