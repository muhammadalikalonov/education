from django.contrib import admin
from .models import *

from modeltranslation.admin import TranslationAdmin




admin.site.register(Rating)


@admin.register(University)
class UniversityAdmin(TranslationAdmin):
    # form = NewsAdminForm
    list_display = ('name', 'university_city',)
    list_filter =('name','university_city')
    prepopulated_fields = {'slug':('name',)}




@admin.register(Study_form)
class Study_formAdmin(TranslationAdmin):
    # form = NewsAdminForm
    list_display = ('name',)
    list_filter =('name',)



@admin.register(Faculty)
class FacultyAdmin(TranslationAdmin):
    # form = NewsAdminForm
    list_display = ('name',)
    list_filter =('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Country)
class CountryAdmin(TranslationAdmin):
    # form = NewsAdminForm
    list_display = ('name', 'banner')
    list_filter =('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Document)
class DocumentAdmin(TranslationAdmin):
    # form = NewsAdminForm
    list_display = ('name', 'need')
    list_filter =('name',)
