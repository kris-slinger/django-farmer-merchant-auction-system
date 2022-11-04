"""server URL Configuration

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
from webbrowser import get
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("auth.urls")),
    path('users/', include("users.urls")),
    path('docs/', include_docs_urls(title="Farmer merchant auction system")),
    path('products/', include("products.urls")),
    path('schema/', get_schema_view(
        title='Farmer merchant auction system',
        description='API for all things',
        version='1.0.0'
    ), name="openapi-schema")
]
