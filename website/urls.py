from django.urls import path
from django.views.generic import TemplateView
from .views import Ex2View

app_name = 'website'

urlpatterns = [
    path('ex1', TemplateView.as_view(template_name='website/ex1.html', extra_context={'title': 'Custom Title'})),
    path('ex2', Ex2View.as_view(), name='example2')

]