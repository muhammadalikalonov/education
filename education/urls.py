"""education URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),

    path('i18n/',include('django.conf.urls.i18n')),

    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += i18n_patterns(
    path('about/' , include('all.about.urls')),
    path('contact/' , include('all.contacts.urls')),
    path('services/' , include('all.service.urls')),
    path('students/' , include('all.students.urls')),
    path('university', include('all.university.urls')),
    path('news/', include('all.news.urls')),
    path('', include('all.main.urls')),
)



handler404 ='all.about.views.error_404_view'
handler4041 ='all.contacts.views.error_404_view'
handler4042 ='all.service.views.error_404_view'
handler4043 ='all.students.views.error_404_view'
handler4044 ='all.university.views.error_404_view'
handler4045 ='all.news.views.error_404_view'
handler4046 ='all.main.views.error_404_view'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
