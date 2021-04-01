from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin



@admin.register(Service_List)
class Service_ListAdmin(TranslationAdmin):

    list_display = ('content', 'id')
    list_filter =('content','id')
