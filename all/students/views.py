from django.shortcuts import render
from .models import *


def students(request):
    students=Students.objects.all()
    context={
        'students':students
    }
    return render(request , 'others/students.html' , context)