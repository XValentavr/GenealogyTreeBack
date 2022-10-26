from django.urls import path

from support.views import CreateTechSupportMessage

urlpatterns = [
    path('api/v1/', CreateTechSupportMessage.as_view()),

]
