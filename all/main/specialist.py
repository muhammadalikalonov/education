from ..main.models import *
from ..university.models import *
from ..contacts.forms import *
from ..news.models import *

def spec(request):
    specialist = Specialist.objects.all().first()
    form =ContactFormForm()
    formi =ContactFormForm2()
    formuz=ContactFormForm3()
    contact = Contact.objects.all().first()
    country = Country.objects.all()
    zayavka = PageFormsuz()
    forming = PageForms()




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




    }
    return context



