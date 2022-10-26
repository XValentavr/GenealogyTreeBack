from django.urls import path, include, re_path
from django.views.generic import TemplateView

from .views import GetUserAfterAuth

urlpatterns = [
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/useruuid/', GetUserAfterAuth.as_view()),
    re_path(r'activate/.*', TemplateView.as_view(template_name='authentication/confirmation.html')),

]
