from django.shortcuts import render
from django.views.generic.base import TemplateView
from website.models import Post
# Create your views here.

class Ex2View(TemplateView):
    """ Template Response Mixin
     Provides a mechanism to construct a TemplateResponse given suitable context.
     Attributes:
     """
    template_name = 'website/ex2.html'
    # template_engine = the name of the template engine to use for loading the template
    # response_class = Custom template loading or custom context object initialization
    # content_type = Default Django uses 'text/html'.

    """get_context_data(**kwargs) is a method inherited from ContentMixin """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.get(id=1)
        context['data'] = 'Context Data for Ex2'
        return context