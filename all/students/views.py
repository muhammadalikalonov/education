from django.shortcuts import render
from .models import *


def error_404_view(request,exception):
    return render(request, 'others/404.html')


def students(request):
    students=Students.objects.all()[:10]
    active = False
    if students.count() > 10:
        active = True

    if request.method == 'POST':
        students = Students.objects.all()
        active = False
    context={
        'students':students,
        'active':active
    }
    return render(request , 'others/students.html' , context)