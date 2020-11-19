from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:pk>/', views.python_details, name="python details"),
    path('<int:pk>/<str:slug>/', views.python_details, name="python details"),
    path('create/', views.create, name="create")
]
