
from django.urls import path,include
from .views import *
urlpatterns = [

    path('', city , name='city' ),
    # path('country/<str:slug>/', lists.as_view(), name='lists' ),
    # path('university/<str:slug>', single.as_view() , name='single' ),
]
