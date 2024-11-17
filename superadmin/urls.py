"""
URL configuration for superadmin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ggg1.restApi import hrViewSet
from django.urls import path, include
from SmAdmin.views import *



router = DefaultRouter()
router.register(r'mymodel',hrViewSet)
# from AdminApp1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('superadmin/app1/',include('AdminApp1.urls')),
    path('superadmin/app2/',include('ggg1.urls')),
    path('superadmin/records/',include('SmAdmin.urls')),
    path('api/', include(router.urls)),
    
]


from django.conf.urls.static import static
from django.conf import  settings

    
urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
