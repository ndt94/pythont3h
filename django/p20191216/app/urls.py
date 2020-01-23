from django.urls import path
from .views import *

urlpatterns = [
    path('hello', hello),
    path('hello2/<name>', hello2)
]