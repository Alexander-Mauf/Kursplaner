"""kursplaner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls import include
from rest_framework.documentation import include_docs_urls
from rest_framework.permissions import IsAuthenticated

admin.site.site_header = 'Kursplaner - Skischule Fichtelberg'

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^docs/', include_docs_urls(title='Pointpro-Secrets-API', permission_classes=(IsAuthenticated,))),
    path('kurse/', include('kurse.urls')),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      re_path(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
