from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    path('', TemplateView.as_view(template_name='authentication/base.html')),

]
