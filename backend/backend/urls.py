from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('users/', include('allUsers.urls')),

    path('auth/', include('authentication.urls')),

    path('profile/<uuid>/', include('userprofile.urls')),

    path('deal/<uuid>/', include('deal.urls')),

    path('tree/<uuid>/', include('tree.urls')),

    path('support/', include('support.urls')),

    path('genealogistbuildstree/', include('genealogistBuildsTree.urls')),
    # re_path('password/.*', SetNewPassword.as_view()),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
