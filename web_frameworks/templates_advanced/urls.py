from django.urls import path

from templates_advanced.views import index

urlpatterns = (
    path('', index, name='templates index'),
)
