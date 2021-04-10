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

# def universtate(request, country_slug):
#
#     c = Country.objects.get(slug=country_slug)
#     country = Country.objects.all()
#     univer = University.objects.filter(country=c)[:10]
#     active =False
#     if univer.count() >10:
#         active =True
#
#     if request.method == 'GET':
#         cou = request.GET.get('country_1')
#         country_view= request.GET.get('country_view')
#         print(country_view)
#         print('hello')
#     if request.method == 'POST':
#         univer = univer = University.objects.filter(country=c).all()
#         active = False
#
#     document = Document.objects.all()
#     study_form = Study_form.objects.all()
#     k=None
#     if univer.exists():
#         print('----')
#         print(univer)
#         for i in univer:
#             k= i.faculty.all()[:5]
#             print(k)
#
#
#     context={
#         'univer':univer,
#         'country':country,
#         'study_form': study_form,
#         'document': document,
#         'active':active,
#         'k':k,
#         'c':c
#
#     }
#     return render(request, 'others/universtate.html', context)



