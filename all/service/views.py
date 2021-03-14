from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *


# Create your views here.
def service(request):
    # services =Service_List.objects.all()
    #
    # one=services[0]
    # two= services[1]
    # three=services[2]
    # four=services[3]
    # five=services[4]
    # six=services[5]
    # seven=services[6]
    # eight=services[7]
    #
    #
    #
    #
    # context={
    #     'services':services,
    #     'one':one,
    #     'two':two,
    #     'three':three,
    #     'four':four,
    #     'five':five,
    #     'six':six,
    #     'seven':seven,
    #     'eight':eight,
    #
    # }
    return render(request , 'top/services.html' )