from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from modeltranslation.admin import TranslationAdmin

class FAQAdminForm(forms.ModelForm):
    questions_ru = forms.CharField(label='Вопросы', widget=CKEditorUploadingWidget())
    answers_ru = forms.CharField(label='Ответы', widget=CKEditorUploadingWidget())
    questions_uz = forms.CharField(label='Вопросы', widget=CKEditorUploadingWidget())
    answers_uz = forms.CharField(label='Ответы', widget=CKEditorUploadingWidget())

    class Meta:
        model = FAQ
        fields = '__all__'


@admin.register(Advantage)
class AdvantageAdmin(TranslationAdmin):
    # form = AdvantageAdminForm
    list_filter =('title',)
    list_display  =('title',)
    # search_fields =
    save_on_top =True
    # save_as_continue =True
    # list_editable =
    # readonly_fields = ('image',)


@admin.register(FAQ)
class FAQAdmin(TranslationAdmin):
    form = FAQAdminForm
    list_filter =('questions','answers')
    list_display  =('questions',)
    # search_fields =
    save_on_top =True
    save_as_continue =True
    # list_editable =
    # readonly_fields = ('image',)

@admin.register(Testimonials)
class TestimonialsAdmin(TranslationAdmin):
    list_filter = ('name',)
    list_display = ('name',)

@admin.register(Specialist)
class SpecialistsAdmin(TranslationAdmin):
    list_filter = ('name',)
    list_display = ('name',)
