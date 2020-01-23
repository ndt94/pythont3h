from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse('hello')

def hello2(request, name):
    return HttpResponse('Hello ' + name)