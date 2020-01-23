from django.db import models

# Create your models here.
class Student(models.Model):
    studentNo = models.CharField(max_length=20, verbose_name='Ma SV', unique=True)
    name = models.CharField(max_length=50, verbose_name='Ten')
    address = models.CharField(max_length=200, verbose_name='Dia chi', blank=True)

    # def createStudent(studentNo, name):
    #     return Student.objects.create(
    #         studentNo=studentNo,
    #         name=name
    #         address=address
    #     )