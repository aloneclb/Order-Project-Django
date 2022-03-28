"""OrderProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # CKEditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
    # # ZMembers App URL's
    path('members/', include('zmembers.urls')),

    # # ZProduct App URL's
    path('product/', include('zproduct.urls', namespace='product')),

    # # Zcard App URL's
    path('order/', include('zcard.urls', namespace='card')),

    # # ZManage App URL's
    path('manage/', include('zmanage.urls')),
    
    # # ZPages App URL's
    path('', include('zpage.urls')), 

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

