from django.core import serializers
from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

def error_404_view(request,exception):
    return render(request, 'others/404.html')


def country_view(request):
    countries = Country.objects.all()
    faculty = Faculty.objects.all()
    study = Study_form.objects.all()


    univer = University.objects.all()
    paginator = Paginator(univer, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {


        'faculty': faculty,
        'countries': countries,
        'study':study,
        'univer':univer,
        'page_obj': page_obj
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



