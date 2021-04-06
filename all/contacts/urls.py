from django.urls import path,include
from .views import *

urlpatterns = [
     path('', contacts , name='contacts' ),
     path('page/', page , name='page' ),


     path('',contact_mobile,name = 'contact_mobile')
]
