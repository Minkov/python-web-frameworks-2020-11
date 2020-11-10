from os.path import join

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

media_files = static(settings.MEDIA_URL, document_root=join(settings.MEDIA_ROOT, 'public'))

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('templates_advanced.urls')),
                  path('pets/', include('resources.urls')),
              ] + media_files

