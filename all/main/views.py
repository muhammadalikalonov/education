from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
# from ..contact.models import Contact
# Create your views here.
from .models import *


def index(request):
    # message = Contact.objects.all().first()
    # testimonials = Testimonials.objects.all()
    #
    # number = FAQ.objects.all().count()
    # column1 = FAQ.objects.all()[:number // 2]
    # column2 = FAQ.objects.all()[number // 2:]
    #
    # advantage = Advantage.objects.all()
    #
    # context = {
    #     'message': message,
    #     'testimonials': testimonials,
    #     'column1': column1,
    #     'column2': column2,
    #     'advantage': advantage,
    #
    # }
    return render(request, 'main/index.html')


def error(request):
    context = {

    }
    return render(request, 'other/error.html', context)






