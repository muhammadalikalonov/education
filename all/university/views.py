from django.core import serializers
from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.views.generic import ListView

from django.core.serializers import serialize




def country_view(request):
    univer = University.objects.all().order_by('-id')
    if request.method =='GET':
        try:
            decrease = request.GET.get('decrease')
            univer = univer.all().order_by('-on_campus_yearly')
        except:
            uncrease = request.GET.get('uncrease')
            univer = univer.all().order_by('on_campus_yearly')
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


# class FilterMoviesView(ListView):
#     model =University
#     context_object_name = 'univer'
#     template_name = 'blog/univers.html'
#
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['faculty'] = Faculty.objects.all()
#         context['countries'] = Country.objects.all()
#         print(context['faculty'])
#         return context
#
#     def get_queryset(self):
#
#         queryset=University.objects.filter(faculty__in=self.request.GET.getlist('faculty'))
#
#         return queryset

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



# def university_view(request):

    # study = Study_form.objects.all()
    # fac = Faculty.objects.all()



    # for i in study:
    #     print(i.studing.all())
    # for i in univer:
    #     print(i.name, i.study_form.all())
    # context = {
        # 'city_london': city_london,
        # 'single': single,
        # 'country': country,
        # 'univer':univer

    # }
    # return render(request, 'blog/univers.html', context)




def universtate(request, country_slug):

    country = Country.objects.get(slug=country_slug)
    univer = University.objects.filter(country=country)
    univer_popular = univer.all().order_by('-id')
    univer_increase = univer.all().order_by('on_campus_yearly')
    univer_decrease = univer.all().order_by('-on_campus_yearly')


    document = Document.objects.all()
    study_form = Study_form.objects.all()
    context={
        'univer':univer,
        'country':country,
        'study_form': study_form,
        'document': document,

    }
    return render(request, 'others/universtate.html', context)



def popular(request):




    # univer = University.objects.all()
    # paginator = Paginator(univer, 5)
    # page_number = request.GET.get('page')
    # posts_obj = paginator.get_page(page_number)
    # univer_popular = univer.all().order_by('-id')
    # univer_increase = univer.all().order_by('on_campus_yearly')
    # univer_decrease = univer.all().order_by('-on_campus_yearly')
    # countries = Country.objects.all()
    # faculty = Faculty.objects.all()
    # study = Study_form.objects.all()
    #
    # context = {
    #
    #     'faculty': faculty,
    #     'countries': countries,
    #     'study': study,
    #     'univer': posts_obj,
    #
    # }
    return request(render, 'others/pop.html')


