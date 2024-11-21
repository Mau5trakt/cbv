from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView, RedirectView
from website.models import Post
from django.db.models import F
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

class PostPreLoadTaskView(RedirectView):
    ''' it can be used with an url attribute or pattern_name attribute
        the pattern_name is the name of an url
    '''
    pattern_name = 'website:singlepost'
    def get_redirect_url(self, *args, **kwargs):
        
        post = get_object_or_404(Post, pk=kwargs['pk'])
        post.count = F('count') +1
        post.save()

        

        return super().get_redirect_url(*args, **kwargs)
    

class SinglePostView(TemplateView):
    template_name ='website/ex4.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        return context
    
    