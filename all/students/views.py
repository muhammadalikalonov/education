from django.shortcuts import render
from .models import *



# Create your views here.
def students(request):
    # galleries=Gallery.objects.all()

    context={
        # 'galleries':galleries

    }
    return render(request , 'top/students.html' , context)