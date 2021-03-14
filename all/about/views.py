from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *
# from ..home.models import *


# Create your views here.

def about(request):
    # section1 = Section_One.objects.all().first()
    # advantage = Advantage.objects.all()
    #
    # section2 = Section_Two.objects.all().first()
    #
    # context = {
    #     'section1': section1,
    #     'section2': section2,
    #     'advantage': advantage,
    #
    # }
    return render(request, 'top/about.html')