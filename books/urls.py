from django.urls import path
from .views import IndexView, BookDetailView, GenreView, AddBookView

app_name = 'books'

urlpatterns = [
     path('', IndexView.as_view(), name='index'),
     path('add', AddBookView.as_view(), name='add_book'),
     path('<slug:slug>', BookDetailView.as_view(), name='book_detail'),
     path('c/<str:genre>', GenreView.as_view(), name='book_genre'),

]