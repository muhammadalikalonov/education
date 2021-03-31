from ..main.models import *
from ..university.models import *
from ..contacts.forms import *
from ..news.models import *

def spec(request):
    specialist = Specialist.objects.all().first()
    form =ContactFormForm()
    formi =ContactFormForm2()
    contact = Contact.objects.all().first()
    country = Country.objects.all()
    forming = PageForms()
    study  = Study_form.objects.all()
    faculty = Faculty.objects.all()
    # university = University.objects.all()
    # for i in country:
    #     print(i.country.all().count())



    context={
        'specialist':specialist,
        'contact':contact,
        'form':form,
        'formi':formi,
        'country':country,
        'study':study,
        'faculty':faculty,
        'forming':forming


    }
    return context



