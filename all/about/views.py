from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *
from ..service.models import *
from ..main.models import *



def about(request):
    section1 = Section_One.objects.all().first()
    service_List = Service_List.objects.all()



    context = {
        'section1': section1,

        'service_List': service_List,
    #
    }
    return render(request, 'others/about.html', context)