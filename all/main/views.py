from django.core import serializers
from django.shortcuts import render
from django.shortcuts import render
from ..university.models import *
from ..students.models import *
# from ..contact.models import Contact
# Create your views here.
from ..news.models import *
from .models import *
from django.core.serializers import serialize
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Max,Min

def filter_data(request):
    # minmaxPrice =University.objects.aggregate(Min('price'),Max('price'))
    # # minPrice = request.GET['minPrice']
    # # maxPrice = request.GET['maxPrice']
    # 	allProducts=allProducts.filter(productattribute__price__gte=minPrice)
    # 	allProducts=allProducts.filter(productattribute__price__lte=maxPrice)
    countrys =request.GET.getlist('country[]')
    study =request.GET.getlist('study[]')
    faculty =request.GET.getlist('faculty[]')


    allProducts = University.objects.all()
    if len(countrys)>0:
        allProducts=allProducts.filter(country__name__in =countrys).distinct()

    if len(study)>0:
        allProducts=allProducts.filter(study_form__name__in=study).distinct()

    if len(faculty)>0:
        allProducts=allProducts.filter(faculty__name__in=faculty).distinct()

    t = render_to_string('blog/ajax/univers.html',{'univer':allProducts})
    return JsonResponse({'univer':t})



def index(request):
    top_university = University.objects.filter(top_universities =True)
    students = Gallery.objects.all()
    university = University.objects.all().count()
    countries =Country.objects.filter(banner=True)
    country = countries.count()
    # for i in countries:
    #     print(i)
    #     coun = University.objects.filter(country = '')

    # message = Contact.objects.all().first()
    testimonials = Testimonials.objects.all()
    faq = FAQ.objects.all()
    # number = FAQ.objects.all().count()
    # column1 = FAQ.objects.all()[:number // 2]
    # column2 = FAQ.objects.all()[number // 2:]

    advantage = Advantage.objects.all()


    context = {
        # 'message': message,
        # 'testimonials': testimonials,
        # 'column1': column1,
        # 'column2': column2,
        'students': students,
        'faq':faq,

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


def load(request):
    offset =int(request.POST['offset'])
    limit= 2
    posts = University.objects.all()[offset:offset+limit]
    totalData = University.objects.count()
    data={}
    posts_json =serializers.serialize('json',posts)
    return JsonResponse(data={'posts':posts_json,
                              'totalResult':totalData})


def loadding(request,*args,**kwargs):
    upper =kwargs.get('num_posts')
    lower =upper -3
    news = list(News.objects.values()[lower:upper])
    news_size =len(News.objects.all())
    size =True if upper>=news_size else False
    return JsonResponse({'news':news,'max':size}, safe=False)




def search(request):
    if request.method == 'GET':
        search_text = request.GET.get('search_text')

    else:
        search_text = ''


    univer =University.objects.filter(name__contains=search_text)
    print(univer)

    t = render_to_string('blog/search.html', {'univer': univer,'search_text':search_text})

    return JsonResponse({'data': t})

