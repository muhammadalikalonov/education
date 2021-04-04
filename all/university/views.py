from django.core import serializers
from django.shortcuts import render
from .models import *
from django.db.models import Min,Max
from django.core.paginator import Paginator
from django.views.generic import ListView

from django.core.serializers import serialize


def error_404_view(request,exception):
    return render(request, 'others/404.html')





def country_view(request):


    univer = University.objects.all().order_by('-id').all()
    if request.method =='POST':
        univer = University.objects.all().order_by('-id').all()
        active = False

    active = False
    if univer.count() > 10:
        active = True

    countries = Country.objects.all()
    faculty = Faculty.objects.all()
    study = Study_form.objects.all()

    for i in univer:
        k= i.faculty.all()[:5]
    print(k)


    context = {


        'faculty': faculty,
        'countries': countries,
        'study':study,
        'univer':univer,
        'k':k,
        'active':active,

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

def universtate(request, country_slug):

    c = Country.objects.get(slug=country_slug)
    country = Country.objects.all()
    univer = University.objects.filter(country=c)[:10]
    active =False
    if univer.count() >10:
        active =True

    if request.method == 'GET':
        cou = request.GET.get('country_1')
        print(cou)
    if request.method == 'POST':
        univer = univer = University.objects.filter(country=c).all()
        active = False

    document = Document.objects.all()
    study_form = Study_form.objects.all()
    for i in univer:
        k= i.faculty.all()[:5]


    context={
        'univer':univer,
        'country':country,
        'study_form': study_form,
        'document': document,
        'active':active,
        'k':k,
        'c':c

    }
    return render(request, 'blog/univers.html', context)



