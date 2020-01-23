from django.shortcuts import render, redirect
from .forms import MailForm, StudentForm
from .models import Student
# Create your views here.
def index(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})

def createStudent(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('home')
            # return render(request, 'success.html')
    return render(request, 'student_form.html', {'form': form})

def updateStudent(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'student_form.html', {'form': form})
