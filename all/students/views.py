from django.shortcuts import render
from .models import *


def students(request):
    students=Students.objects.all()
    if request.method == 'POST':
        print('asd')
        students = Students.objects.all()[:6]

    context={
        'students':students
    }
    return render(request , 'others/students.html' , context)