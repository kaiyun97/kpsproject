"""
URL configuration for kpsproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from myapp.views import hello,Stype,Ctype,Rtype,Etype,Itype,Atype,group,question,video,contact,news

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',hello),
    path('Stype/',Stype),
    path('Ctype/',Ctype),
    path('Rtype/',Rtype),
    path('Etype/',Etype),
    path('Itype/',Itype),
    path('Atype/',Atype),
    path('group/',group),
    path('question/',question),
    path('video/',video),
    path("contact", contact),
    path("news/", news),
]
