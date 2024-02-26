# seu_app/urls.py
from django import views
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", include('todos.urls')),
    path("admin/", admin.site.urls),
    path('account/', include('account.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path("ckeditor/", include('ckeditor_uploader.urls')),
    
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


