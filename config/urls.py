# -*- coding: utf-8 -*-
"""gromov URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from girls.views import GirlsListView, GirlDetailView
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve
from django.conf.urls.static import static


urlpatterns = [
    url('admin/', admin.site.urls),
    url('models/', GirlsListView.as_view(), name='girls-list'),
    url('girl/<int:id>', GirlDetailView.as_view(), name='girl-detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
