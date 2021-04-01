from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from modeltranslation.admin import TranslationAdmin


class Section_OneAdminForm(forms.ModelForm):
    content_ru = forms.CharField(label='Описание на рус', widget=CKEditorUploadingWidget())
    content_uz = forms.CharField(label='Описание на узб', widget=CKEditorUploadingWidget())
    class Meta:
        model = Section_One
        fields = '__all__'


@admin.register(Section_One)
class AdvantageAdmin(TranslationAdmin):
    form = Section_OneAdminForm

    # search_fields =
    save_on_top =True
    # save_as_continue =True
    # list_editable =
    # readonly_fields = ('image',)


