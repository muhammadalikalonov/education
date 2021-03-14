from django.shortcuts import render
from django.shortcuts import render
# from ..contact.models import Contact
# Create your views here.
from .models import *


# Create your views here.
def news(request):

    context={

    }
    return render(request , 'other/error.html' , context)


