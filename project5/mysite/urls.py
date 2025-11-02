"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

import os

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [path("admin/", admin.site.urls), path("", include("home.urls"))]

# Serve static files
# In Docker, collectstatic runs, so files are in STATIC_ROOT
# Otherwise, serve from STATICFILES_DIRS (development)
if os.path.exists(settings.STATIC_ROOT):
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    # In development, also serve from STATICFILES_DIRS
    urlpatterns += staticfiles_urlpatterns()
