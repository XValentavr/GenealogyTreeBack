from django.urls import path

from allUsers.views import GetAllUsersToCheckIsGenealogist

urlpatterns = [
    path('api/v1/fetch/', GetAllUsersToCheckIsGenealogist.as_view()),
]
