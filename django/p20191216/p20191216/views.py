from django.shortcuts import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def hello(request):
    if request.method == 'GET':
        name = request.GET.get('name', '')
        gender = request.GET.get('gender')
    else:
        name = request.POST.get('name', '')
        gender = request.POST.get('gender')
    salute = 'Mr' if gender == 'M' else 'Ms'
    return HttpResponse(f'Hello {salute} {name}')

def hello2(request, name):
    return HttpResponse('Hello ' + name)