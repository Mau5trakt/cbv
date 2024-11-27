from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from books.models import Book
from django.db.models import F
from django.utils import timezone
# Create your views here.
"""
    Detail View have to be called by his pk or slug
    <int:pk> <slug:slug>
"""


class IndexView(ListView):
    
    model = Book
    template_name = "home.html"
    context_object_name = 'books'
    paginate_by = 4


    def get_queryset(self):
        return Book.objects.all()[:3]
    
class BookDetailView(DetailView):
    model = Book
    
    # By default django will look for book_detail template 
    # <modelname_detail>
    
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = Book.objects.filter(slug=self.kwargs.get('slug'))
        post.update(count=F('count') + 1)
        
        context['time'] = timezone.now()

        return context

class GenreView(ListView):
    model = Book
    template_name = 'home.html'
    paginate_by = 2
    context_object_name = 'books'

    def get_queryset(self, *args, **kwargs):
        return Book.objects.filter(genre__contains=self.kwargs.get('genre'))