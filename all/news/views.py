from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from ..news.models import *
# from ..contact.models import Contact
# Create your views here.
from .models import *
from django.core import serializers

# Create your views here.
def news(request):
    news = News.objects.all()
    context={
        'news':news,
    }
    return render(request , 'blog/news.html' , context)


def article(request, slug):
    article = News.objects.get(slug =slug, top_news=True, banner=True)

    new_article = News.objects.all().order_by('-id')[:3]
    context={
        'article':article,
        'new_article':new_article

    }
    return render(request , 'blog/article.html' , context)


def load_more(request):
    offset = int(request.POST['offset'])
    limit =1
    news =News.objects.all()[offset:limit+offset]
    totalData=News.objects.count()

    data={}
    posts_json =serializers.serialize('json',news)


    return  JsonResponse(data={
        'news':posts_json,
        'totalResult':totalData
    })