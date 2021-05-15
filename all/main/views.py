from django.core import serializers
from django.shortcuts import render
from django.shortcuts import render
from ..university.models import *
from ..students.models import *
# from ..contact.models import Contact
# Create your views here.
from ..news.models import *
from .models import *
from django.core.paginator import Paginator
from django.core.serializers import serialize
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Max,Min

def error_404_view(request,exception):
    return render(request, 'others/404.html')




def filter_data(request):


    univer = University.objects.get_queryset().order_by('id')

    search_text = request.GET.get('search_text')

    if search_text:
        univer = University.objects.filter(name__icontains=search_text)

    countrys =request.GET.getlist('country[]')
    study =request.GET.getlist('study[]')
    facultys =request.GET.getlist('faculty[]')


    if request.GET.get('minPrice') == 'true':
        univer = univer.order_by('year_tuition_fee')

    if request.GET.get('maxPrice') == 'true':
        univer = univer.order_by('-year_tuition_fee')

    if request.GET.get('popPrice') == 'true':
        univer = univer.order_by('-rating_id')

    if len(facultys)>0:

        univer=univer.filter(faculty__name__in=facultys).distinct()

    if len(countrys)>0:
        univer=univer.filter(country__name__in =countrys).distinct()

    if len(study)>0:
        univer=univer.filter(study_form__name__in=study).distinct()

    paginator = Paginator(univer, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(page_obj)


    data={
        'page_obj': page_obj,
        'univer': univer,
        'search_text': search_text
    }

    t = render_to_string('blog/ajax/univers.html', data)
    # print(t)
    return JsonResponse({'univer':t})




def index(request):
    top_university = University.objects.filter(top_universities =True)
    students = Gallery.objects.all()
    university = University.objects.all().count()
    countries =Country.objects.filter(banner=True)
    country = countries.count()

    testimonials = Testimonials.objects.all()
    faq = FAQ.objects.all()
    advantage = Advantage.objects.all()


    context = {

        'students': students,
        'faq': faq,
        'advantage': advantage,
        'top_university':top_university,
        'university':university,
        'country':country,
        'countries':countries,
        'testimonials':testimonials

    }
    return render(request, 'base/index.html',context)


def error(request):
    context = {

    }
    return render(request, 'others/404.html', context)


def page(request):
    context = {

    }
    return render(request, 'others/cons.html', context)




def loadding(request,*args,**kwargs):
    upper =kwargs.get('num_posts')
    lower =upper -3
    news = list(News.objects.values()[lower:upper])
    news_size =len(News.objects.all())
    size =True if upper>=news_size else False
    return JsonResponse({'news':news,'max':size}, safe=False)





