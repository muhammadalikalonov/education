from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


@admin.register(Consulting)
class ConsultingAdmin(admin.ModelAdmin):
    # form = AdvantageAdminForm
    list_filter =('name','surname','phone','english','study','take_date','date')
    list_display  =('name','surname','phone','english','study','take_date','date')
    search_fields =('name','phone')
    save_on_top =True
    date_hierarchy = 'date'
    # save_as_continue =True
    # list_editable =
    # readonly_fields = ('image',)

@admin.register(Contact_Form)
class Contact_FormAdmin(admin.ModelAdmin):
    # form = AdvantageAdminForm
    list_filter =('name','phone','content','date')
    list_display  =('name','phone','content','date')
    search_fields =('name','phone')
    save_on_top =True
    date_hierarchy = 'date'
    # save_as_continue =True
    # list_editable =
    # readonly_fields = ('image',)




@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display  =('phone','telegram','facebook','instagram','working_time','address')
    search_fields =('phone',)
    save_on_top =True



@admin.register(Consulting_uz)
class Consulting_uzAdmin(admin.ModelAdmin):
    # form = AdvantageAdminForm
    list_filter =('name','surname','phone','english','study','take_date','date')
    list_display  =('name','surname','phone','english','study','take_date','date')
    search_fields =('name','phone')
    save_on_top =True
    date_hierarchy = 'date'
    # save_as_continue =True
    # list_editable =
    # readonly_fields = ('image',)