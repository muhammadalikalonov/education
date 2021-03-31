from modeltranslation.translator import register, TranslationOptions
from .models import *
from ..news.models import *
from ..university.models import *
from ..contacts.models import *

from ..service.models import *
from ..students.models import *
from ..about.models import *



@register(Specialist)
class SpecialistTranslationOptions(TranslationOptions):
    fields = ('name', 'status')


@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('questions', 'answers')


@register(Advantage)
class AdvantageTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Testimonials)
class TestimonialsTranslationOptions(TranslationOptions):
    fields = ('name','content')


@register(Section_One)
class Section_OneTranslationOptions(TranslationOptions):
    fields = ('content',)


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Service_List)
class Service_ListTranslationOptions(TranslationOptions):
    fields = ('content',)


@register(Students)
class StudentsTranslationOptions(TranslationOptions):
    fields = ('name', 'content')


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Faculty)
class FacultyTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Study_form)
class Study_formTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(University)
class UniversityTranslationOptions(TranslationOptions):
    fields = ('name', 'university_city','language','content','intake')

@register(Document)
class DocumentTranslationOptions(TranslationOptions):
    fields = ('name',)