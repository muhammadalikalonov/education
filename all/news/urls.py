from django.urls import path, include
from .views import *

urlpatterns = [
    path('', news, name='news'),
    # path('success/', error, name='error'),

]
