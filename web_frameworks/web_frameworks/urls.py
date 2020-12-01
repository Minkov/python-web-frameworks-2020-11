from os.path import join

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

media_files = static(settings.MEDIA_URL, document_root=join(settings.MEDIA_ROOT, 'public'))

urlpatterns = [
                  path('rest-api/', include('rest_framework.urls')),
                  path('auth/token/', obtain_auth_token, name='api_token_auth'),
                  path('admin/', admin.site.urls),
                  path('', include('templates_advanced.urls')),
                  path('pets/', include('resources.urls')),
                  path('cbv/', include('cbv.urls')),
                  path('api/books/', include('books_api.urls')),
                  path('books/', include('books.urls')),
              ] + media_files

handler404 = 'web_frameworks.views.handler400'
