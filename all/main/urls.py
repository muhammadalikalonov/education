from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('success/', error, name='error'),
    path('filter/', filter_data, name='filter_data'),
    path('loading/<int:num_posts>/', loadding, name='loading'),
    path('load_students/<int:num_posts>/', load_students, name='load_students'),
    path('search/',search , name='search'),



]
