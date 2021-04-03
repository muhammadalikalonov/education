from django.core import serializers
from django.shortcuts import render
from .models import *
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
        a=request.POST.get('popular')
        if request.POST.get('decrease'):
            univer = University.objects.all().order_by('-year_tuition_fee')
            print('decrease')
        if request.GET.get('increase'):
            print('inc')
            univer = University.objects.all().order_by('year_tuition_fee')
        else:
            univer = University.objects.all().order_by('-id')

    active = False
    if univer.count() > 10:
        active = True

    countries = Country.objects.all()
    faculty = Faculty.objects.all()
    study = Study_form.objects.all()
    for i in univer:
        k= i.faculty.all()[:5]



    context = {


        'faculty': faculty,
        'countries': countries,
        'study':study,
        'univer':univer,
        'k':k,
        'active':active

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

    univer = University.objects.filter(country=country)[:10]
    active =False
    if univer.count() >10:
        active =True
    if request.method == 'POST':
        univer = univer = University.objects.filter(country=country).all()
        active = False

    document = Document.objects.all()
    study_form = Study_form.objects.all()
    context={
        'univer':univer,
        'country':country,
        'study_form': study_form,
        'document': document,
        'active':active

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


