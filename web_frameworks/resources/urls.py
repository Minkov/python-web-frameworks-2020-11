from django.urls import path

from resources.views import pets, get_private_file

urlpatterns = (
    path('', pets, name='pets'),
    path('resources/<path:path_to_file>/', get_private_file, name='private file')
)
