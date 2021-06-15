from django.core import serializers
from django.shortcuts import render
from .models import *


def error_404_view(request, exception):
    return render(request, 'others/404.html')


def country_view(request):
    countries = Country.objects.all()
    faculty = Faculty.objects.all()
    study = Study_form.objects.all()
    univer = University.objects.all()
    # page = request.GET.get('page', 1)
    # paginator = Paginator(univer, 1)
    # try:
    #     users = paginator.page(page)
    # except PageNotAnInteger:
    #     users = paginator.page(1)
    # except EmptyPage:
    #     users = paginator.page(paginator.num_pages)
    # print(users.has_other_pages)
    # for i in users.paginator.page_range:
    #     print(i)
    context = {
        'faculty': faculty,
        'countries': countries,
        'study': study,
        'univer': univer
    }
    return render(request, 'blog/univers.html', context)


from django.shortcuts import get_object_or_404


def uninfo(request, slug):
    univer = get_object_or_404(University, slug=slug)
    document = Document.objects.all()
    study_form = Study_form.objects.all()
    faculty_formsss = Faculty_for_Forms.objects.filter(content__name=univer.name)
    context = {
        'study_form': study_form,
        'document': document,
        'univer': univer,
        'faculty_formsss': faculty_formsss
    }
    return render(request, 'blog/uninfo.html', context)
