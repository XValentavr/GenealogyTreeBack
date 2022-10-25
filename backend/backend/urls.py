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

    path('tree/<uuid>/', include('tree.urls')),

    re_path('password/.*', SetNewPassword.as_view()),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
