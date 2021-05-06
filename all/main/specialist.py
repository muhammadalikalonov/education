from ..main.models import *
from ..university.models import *
from ..contacts.forms import *
from ..news.models import *
from django.core.paginator import Paginator
def spec(request):
    specialist = Specialist.objects.all().first()
    form =ContactFormForm()
    formi =ContactFormForm2()
    formuz=ContactFormForm3()
    contact = Contact.objects.all().first()
    country = Country.objects.all()
    zayavka = PageFormsuz()
    forming = PageForms()
    univer = University.objects.all()
    paginator = Paginator(univer, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    study  = Study_form.objects.all()
    faculty = Faculty.objects.all()



    context={
        'specialist':specialist,
        'contact':contact,
        'form':form,
        'formi':formi,
        'country':country,
        'study':study,
        'faculty':faculty,
        'zayavka': zayavka,
        'forming':forming,
        'formuz':formuz,
        'page_obj': page_obj




    }
    return context



