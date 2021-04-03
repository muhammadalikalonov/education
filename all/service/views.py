from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *
def error_404_view(request,exception):
    return render(request, 'others/404.html')

# Create your views here.
def service(request):
    services =Service_List.objects.all()

    context={
        'services':services,

    }
    return render(request , 'others/uslugi.html', context )