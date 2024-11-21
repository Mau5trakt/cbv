from django.urls import path
from django.views.generic import TemplateView, RedirectView
from .views import Ex2View, PostPreLoadTaskView, SinglePostView

app_name = 'website'

urlpatterns = [
    path('ex1', TemplateView.as_view(template_name='website/ex1.html', extra_context={'title': 'Custom Title'})),
    path('ex2', Ex2View.as_view(), name='example2'),
    path('rdt', RedirectView.as_view(url='https://www.google.com'), 
         name='redirect'),
    path('ex3/<int:pk>', PostPreLoadTaskView.as_view(), name='redirect-task'),
    path('ex4/<int:pk>', SinglePostView.as_view(), name='singlepost'), 
]