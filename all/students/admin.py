from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin



admin.site.register(Gallery)

@admin.register(Students)
class StudentsAdmin(TranslationAdmin):
    # form = NewsAdminForm
    list_display = ('name', 'university','content','date')
    list_filter =('name','content')
