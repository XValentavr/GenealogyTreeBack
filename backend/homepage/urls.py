from django.urls import path

from homepage import views

app_name = 'backend'
urlpatterns = [
    path('', views.index, name='index'),

]
