from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from modeltranslation.admin import TranslationAdmin

# class NewsAdminForm(forms.ModelForm):
#     description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
#
#     class Meta:
#         model = News
#         fields = '__all__'


@admin.register(News)
class NewsAdmin(TranslationAdmin):
    # form = NewsAdminForm
    list_display = ('name','banner', 'top_news','date')
    list_filter =('name','banner','top_news','date')
    ordering = ('-id',)
    search_fields = ('name','description','id','date')
    save_on_top =True
    save_as_continue =True
    prepopulated_fields = {'slug':('name',)}
    # list_editable =('description','name')
    # readonly_fields = ('image',)



