from .models import *
from django import forms
from ..university.models import *
from django.forms.widgets import RadioSelect
from modeltranslation.forms import TranslationModelForm


class ContactFormForm(TranslationModelForm):
    class Meta:
        model = Contact_Form
        fields = ['name', 'phone', 'content']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': "input form__input _name _req", 'id': 'form_id_afassdsdwdwfas','data-value': "Ваше имя", 'name': "form[]",
                       'type': "text",'required': '', 'autocomplete': "off"}),
            'phone': forms.TextInput(
                attrs={'class': "input form__input _phone _req _tel",'id': 'form_id_asdnamewefwef', 'data-value': "+998 (93) 563-55-09",
                       'name': "form[]", 'type': "text",'required': '', 'autocomplete': "off"}),
            'content': forms.Textarea(
                attrs={'class': "form__input input _msg", 'id': 'form_id_nwqeqwamehhj','data-value': "Дополнительные комментарии", 'rows': "10",
                       'cols': "30", 'name': "txt", 'required': '', 'placeholder': 'Text'}),
        }



class ContactFormForm2(TranslationModelForm):
    class Meta:
        model = Contact_Form
        fields = ['name', 'phone', 'content']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': "input form__input _name _req", 'id': 'form_id_afasfas','data-value': "Ваше имя", 'name': "form[]",
                       'type': "text",'required': '', 'autocomplete': "off"}),
            'phone': forms.TextInput(
                attrs={'class': "input form__input _phone _req _tel",'id': 'form_id_namewefwef', 'data-value': "+998 (93) 563-55-09",
                       'name': "form[]", 'type': "text",'required': '', 'autocomplete': "off"}),
            'content': forms.Textarea(
                attrs={'class': "form__input input _msg", 'id': 'form_id_namehhj','data-value': "Дополнительные комментарии", 'rows': "10",
                       'cols': "30", 'name': "txt", 'required': '', 'placeholder': 'Text'}),
        }

class ContactFormForm3(TranslationModelForm):
    class Meta:
        model = Contact_Form
        fields = ['name', 'phone', 'content']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': "input form__input _name _req", 'id': 'form_id_afasfas1','data-value': "Ismingiz", 'name': "form[]",
                       'type': "text",'required': '', 'autocomplete': "off"}),
            'phone': forms.TextInput(
                attrs={'class': "input form__input _phone _req _tel",'id': 'form_id_namewefwef2', 'data-value': "+998 (93) 563-55-09",
                       'name': "form[]", 'type': "text",'required': '', 'autocomplete': "off"}),
            'content': forms.Textarea(
                attrs={'class': "form__input input _msg", 'id': 'form_id_namehhj3','data-value': "Qo'shimcha ma'lumot", 'rows': "10",
                       'cols': "30", 'name': "txt", 'required': '', 'placeholder': 'Text'}),
        }






level_up = (('Boshlang`ich (А1-А2)', 'Boshlang`ich (А1-А2)'), ('O`rtacha (В1-В2)', 'O`rtacha (В1-В2)'),
         ('Mukammal (С1-С2)', 'Mukammal (С1-С2)'))

study_up = (('Bakalavr', 'Bakalavr'), ("Foundation", "Foundation"), ('Magistratura', 'Magistratura'))




class PageFormsuz(TranslationModelForm):
    english = forms.CharField(  label='English',widget=forms.RadioSelect(choices=level_up))

    study = forms.CharField( label='Study ',widget=forms.RadioSelect(choices=study_up))

    class Meta:
        model = Consulting_uz
        fields = ['name', 'birth_date', 'city', 'email', 'english', 'study', 'description', 'take_date', 'phone',
                  'surname']
        widgets = {

            'name': forms.TextInput(
                attrs={'class': "input form__input _req", 'id': 'formwdq_id_name', 'data-value': "Ismingiz", 'name': "1form[]",
                       'type': "text"}),
            'surname': forms.TextInput(
                attrs={'class': "input form__input _req", 'id': 'form_wdid_surname', 'data-value': "Familiyangiz",
                       'name': "1form[]",
                       'type': "text"}),

            'birth_date': forms.DateInput(
                attrs={'class': "input form__input _req", 'id': 'form_dwqid_birth', 'data-min': '1990',
                       'data-value': "Tug'ilgan sa'na", 'data-max': '2020', 'name': "1form[]",
                       'type': "date"}),

            'city': forms.TextInput(
                attrs={'class': "input form__input _req", 'id': 'foqdwrm_id_syti', 'data-value': "Shahringiz", 'name': "1form[]",
                       'type': "text"}),

            'phone': forms.TextInput(
                attrs={'class': "input form__input _phone _req", 'id': 'formqwd_id_text',
                       'data-value': "+998 (93) 563 - 55 - 09", 'name': "1form[]",
                       'type': "text"}),
            'email': forms.EmailInput(
                attrs={'class': "input form__input _email _req", 'id': 'form_iqwdd_email', 'data-value': "E-mail",
                       'name': "1form[]",
                       'type': "email"}),

            'description': forms.Textarea(
                attrs={'cols': "30", 'rows': "10", 'class': "form__input input _msg", 'id': 'foqwdrm_id',
                       'data-value': "Qo'shimcha ma'lumot",
                       'name': "1comment", 'type': "text"}),

            'take_date': forms.DateInput(
                attrs={'class': "input form__input _req", 'data-min': '1990', 'id': 'fqwdorm_id_req', 'data-value': "Topshirish kuni",
                       'data-max': '2020',
                       'name': "1form[]", 'type': "date"}),
        }




level = (('Начинающий (А1-А2)', 'Начинающий (А1-А2)'), ('Средний (В1-В2)', 'Средний (В1-В2)'),
         ('Продвинутый(С1-С2)', 'Продвинутый(С1-С2)'))

study = (('Бакалавр', 'Бакалавр'), ("Foundation", "Foundation"), ('Магистратура', 'Магистратура'))


class PageForms(TranslationModelForm):
    english = forms.CharField(  label='Study form', help_text='He забудьте задать рубрику!',
                                  widget=forms.RadioSelect(choices=level, attrs={ 'name': "1" ,'data-value':""}))

    study = forms.CharField(
                              label='Study form', help_text='He забудьте задать рубрику!',
                              widget=forms.RadioSelect(choices=study))

    class Meta:
        model = Consulting
        fields = ['name', 'birth_date', 'city', 'email', 'english', 'study', 'description', 'take_date', 'phone',
                  'surname']
        widgets = {

            'name': forms.TextInput(
                attrs={'class': "input form__input _req", 'id': 'form_id_name', 'data-value': "Имя", 'name': "form[]",
                       'type': "text"}),
            'surname': forms.TextInput(
                attrs={'class': "input form__input _req", 'id': 'form_id_surname', 'data-value': "Фамилия",
                       'name': "form[]",
                       'type': "text"}),

            'birth_date': forms.DateInput(
                attrs={'class': "input form__input _req", 'id': 'form_id_birth', 'data-min': '1990',
                       'data-value': "День", 'data-max': '2020', 'name': "form[]",
                       'type': "date"}),

            'city': forms.TextInput(
                attrs={'class': "input form__input _req", 'id': 'form_id_syti', 'data-value': "Город", 'name': "form[]",
                       'type': "text"}),

            'phone': forms.TextInput(
                attrs={'class': "input form__input _phone _req", 'id': 'form_id_text',
                       'data-value': "+998 (93) 563 - 55 - 09", 'name': "form[]",
                       'type': "text"}),
            'email': forms.EmailInput(
                attrs={'class': "input form__input _email _req", 'id': 'form_id_email', 'data-value': "E-mail",
                       'name': "form[]",
                       'type': "email"}),

            'description': forms.Textarea(
                attrs={'cols': "30", 'rows': "10", 'class': "form__input input _msg", 'id': 'form_id',
                       'data-value': "Дополнительная информация",
                       'name': "comment", 'type': "text"}),

            'take_date': forms.DateInput(
                attrs={'class': "input form__input _req", 'data-min': '1990', 'id': 'form_id_req', 'data-value': "День",
                       'data-max': '2020',
                       'name': "form[]", 'type': "date"}),
        }




