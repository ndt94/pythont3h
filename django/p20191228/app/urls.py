from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('create_student', createStudent, name='student-create'),
    path('update_student/<int:id>', updateStudent, name='update-student')
]