from django.urls import path, include
from .views import RegisterView, ResetPassword

urlpatterns = [
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    path('', RegisterView.as_view()),
    path('reset/', ResetPassword.as_view())

]
