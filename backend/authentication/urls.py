from django.urls import path
from django.views.generic import TemplateView
from rest_framework_simplejwt import views as jwt_views

app_name = 'backend'
urlpatterns = [
    path('', TemplateView.as_view(template_name="authentication/base.html")),
    path('api/v1/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
