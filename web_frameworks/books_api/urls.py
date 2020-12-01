from django.urls import path

from books_api.views import BooksListApiView, BookDetailsApiView

urlpatterns = (
    path('', BooksListApiView.as_view(), name='books list api'),
    path('<int:pk>/', BookDetailsApiView.as_view(), name='books details api'),
)
