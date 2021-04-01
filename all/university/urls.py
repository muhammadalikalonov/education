
from django.urls import path,include
from .views import *


urlpatterns = [
    path('', country_view , name='country_view' ),
    path('counrty/<str:country_slug>', universtate , name='universtate' ),
    path('univer/<str:slug>/', uninfo , name='uninfo' ),

    path('p/', popular, name='popular'),




    # path('country/<str:slug>/', lists.as_view(), name='lists' ),
    # path('university/<str:slug>', single.as_view() , name='single' ),
]
