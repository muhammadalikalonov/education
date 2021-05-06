from django.core import serializers
from django.shortcuts import render
from .models import *

def error_404_view(request,exception):
    return render(request, 'others/404.html')





def country_view(request):


    univer = University.objects.all()
    countries = Country.objects.all()
    faculty = Faculty.objects.all()
    study = Study_form.objects.all()

    context = {


        'faculty': faculty,
        'countries': countries,
        'study':study,
        'univer':univer,



    }
    return render(request, 'blog/univers.html', context)


from django.shortcuts import get_object_or_404



def uninfo(request, slug):
    univer = get_object_or_404(University, slug=slug)

    document = Document.objects.all()
    study_form = Study_form.objects.all()



    context = {
        'study_form': study_form,
        'document': document,
        'univer':univer,


    }

    return render(request, 'blog/uninfo.html', context)



