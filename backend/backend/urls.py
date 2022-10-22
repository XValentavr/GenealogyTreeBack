"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include, re_path

from authentication.views import SetNewPassword, GetUserUUIDToChangeDeal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('auth/', include('authentication.urls')),
    path('register/', include('register.urls')),
    path('logout/', LogoutView.as_view()),
    path('profile/<uuid>/', include('userprofile.urls')),
    path('deal/api/v1/uuid/', GetUserUUIDToChangeDeal.as_view()),
    path('deal/<uuid>/', include('deal.urls')),

    re_path('password/.*', SetNewPassword.as_view()),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
