from django.urls import path
from django.views.generic import TemplateView

app_name = 'backend'
urlpatterns = [
    path('', TemplateView.as_view(template_name='homepage/base.html')),

]
