from django.urls import path
from . import views
from .views import PythonCreateView

urlpatterns = [
    # path('', views.index, name="index"),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.python_details, name="python details"),
    path('<int:pk>/<str:slug>/', views.python_details, name="python details"),
    path('create/', PythonCreateView.as_view(), name='create'),
    # path('create/', views.create, name="create")
]
