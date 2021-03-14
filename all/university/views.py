from django.shortcuts import render
from .models import *
from django.views.generic.detail import DetailView
from django.views.generic import View, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

#
# class single(DetailView):
#     model = University
#     template_name = 'other/university-single.html'
#     context_object_name = 'university_name'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['page'] = self.request.GET.get('page')
#         context['co'] = Faculty.objects.all().count()
#         if Faculty.objects.all().count() > 9:
#             context['faculty1'] = context['university_name'].faculty.all()[:5]
#             context['faculty2'] = context['university_name'].faculty.all()[5:]
#         else:
#             context['faculty1'] = context['university_name'].faculty.all()
#
#         return context
#
#
# class lists(View):
#
#     def get(self, request, slug):
#         country_university = University.objects.all()
#         country_name = Country.objects.get(slug=slug)
#
#         con = University.objects.filter(country__name=country_name)
#
#         context = {'country_name': country_name,
#                    'country_university': country_university,
#                    'con': con,
#
#                    }
#         return render(request, template_name='other/university-list.html', context=context)
#

def city(request):
    # city_london = Country.objects.filter(name='london')
    # single = Country.objects.filter(banner=True).first()
    # country = Country.objects.exclude(banner=True)

    context = {
        # 'city_london': city_london,
        # 'single': single,
        # 'country': country,

    }
    return render(request, 'top/city-all.html', context)