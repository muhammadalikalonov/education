from django.urls import path, include
from .views import *

urlpatterns = [
    path('', news, name='news'),
    path('<str:slug>/', article, name='article'),
    path('load_more/',load_more,name= 'load_more')


]
