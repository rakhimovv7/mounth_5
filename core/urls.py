"""
URL configuration for core project.

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
from django.conf.urls.static import static
from django.conf import settings

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# drf_yasg
schema_view = get_schema_view(
   openapi.Info(
      title="17-1B API",
      default_version='v1',
      description="17-1B description",
      terms_of_service="https://t.me/Geeks_Osh_bot",
      contact=openapi.Contact(email="abdykadyrovsyimyk0708@gmail.com"),
      license=openapi.License(name="BSD License"), 
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/settings/',include('apps.settings.urls')),
    path('api/v1/news/',include('apps.news.urls')),
    path('api/v1/',include('apps.todolist.urls')),

    #   drf_yasg
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 
]   

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)