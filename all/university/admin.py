from django.contrib import admin
from .models import *

from modeltranslation.admin import TranslationAdmin

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class UniversityAdminForm(forms.ModelForm):
    content_ru = forms.CharField(label='Описание на русском', widget=CKEditorUploadingWidget())
    content_uz = forms.CharField(label='Описание на узбекском', widget=CKEditorUploadingWidget())
    
    
    class Meta:
        model = University 
        fields = '__all__'



admin.site.register(Rating)


@admin.register(University)
class UniversityAdmin(TranslationAdmin):
    form = UniversityAdminForm
    list_display = ('name', 'university_city', 'language', 'year', 'rating', 'intake','year_tuition_fee','on_campus_yearly','top_universities')
    list_filter =('name','university_city','language', 'year', 'rating', 'intake','year_tuition_fee','on_campus_yearly' )
    prepopulated_fields = {'slug':('name',)}
    save_as_continue = True
    save_on_top = True



@admin.register(Study_form)
class Study_formAdmin(TranslationAdmin):
    # form = NewsAdminForm
    list_display = ('name',)
    list_filter =('name',)
    save_as_continue = True
    save_on_top = True


@admin.register(Faculty)
class FacultyAdmin(TranslationAdmin):
    # form = NewsAdminForm
    list_display = ('name','study_year','id')
    list_filter =('name',)
    prepopulated_fields = {'slug': ('name',)}
    save_as_continue = True
    save_on_top = True


@admin.register(Country)
class CountryAdmin(TranslationAdmin):
    # form = NewsAdminForm
    list_display = ('name', 'banner')
    list_filter =('name',)
    prepopulated_fields = {'slug': ('name',)}
    save_as_continue = True
    save_on_top = True
@admin.register(Document)
class DocumentAdmin(TranslationAdmin):
    # form = NewsAdminForm
    list_display = ('name', 'need')
    list_filter =('name',)
    save_as_continue = True
    save_on_top = True