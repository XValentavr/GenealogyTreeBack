from django.urls import path

from tree.views import GetRootUserInfirmation

urlpatterns = [
    path('api/v1/fetch/', GetRootUserInfirmation.as_view()),

]
