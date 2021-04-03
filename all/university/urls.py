
from django.urls import path,include
from .views import *


urlpatterns = [
    path('', country_view , name='country_view' ),
    path('=<str:country_slug>', universtate , name='universtate'),
    path('univer/<str:slug>/', uninfo , name='uninfo' ),

]
