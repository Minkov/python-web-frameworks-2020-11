from django.urls import path
from django.views.generic import TemplateView

from cbv.views import IndexView, IndexTemplateView, PetsListView, PetDetailsView, PetCreateView

urlpatterns = (
    path('', IndexView.as_view(), name='cbv index'),
    path('2/', IndexTemplateView.as_view(), name='cbv index 2'),
    path('3/', TemplateView.as_view(template_name='cbv/index.html')),
    path('list/', PetsListView.as_view(), name='cbv pets list'),
    path('details/<int:pk>', PetDetailsView.as_view(), name='cbv pets details'),
    path('create/', PetCreateView.as_view(), name='cbv pet create'),
)
