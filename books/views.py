from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from books.models import Book
from django.db.models import F
from django.utils import timezone
# Create your views here.
"""
    Detail View have to be called by his pk or slug
    <int:pk> <slug:slug>
"""


class IndexView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context
    
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