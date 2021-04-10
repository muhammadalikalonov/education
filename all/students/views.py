from django.shortcuts import render
from .models import *


def error_404_view(request,exception):
    return render(request, 'others/404.html')


def students(request):
    students=Students.objects.all()[:10]

    context={
        'students':students,

    }
    return render(request , 'others/students.html' , context)