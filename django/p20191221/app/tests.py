from django.test import TestCase
from app.models import Student


# python3 manage.py makemigrations
# python3 manage.py migrate

def getAllStudents():
    return Student.objects.all()

def createStudent(studentNo, name):
    return Student.objects.create(
        studentNo=studentNo,
        name=name
    )

def getStudent(id):
    return Student.objects.get(id=id)

def updateStudent(id, studentNo, name):
    st = getStudent(id)
    st.studentNo = studentNo
    st.name = name
    st.save()
    return st

def deleteStudent(id):
    st = getStudent(id)
    st.delete()


# Create your tests here.
