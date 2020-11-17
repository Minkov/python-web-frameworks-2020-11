from django.urls import path

from resources.views import pets, get_private_file, get_public_file

urlpatterns = (
    path('', pets, name='pets'),
    path('resources_private/<path:path_to_file>/', get_private_file, name='private file'),
    path('resources_public/<path:path_to_file>/', get_public_file, name='public file')
)
