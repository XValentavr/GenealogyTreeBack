from django.urls import path

from tree.views import GetRootUserInfirmation, InsertWifeToRootTree,InsertSpouseToRootTree

urlpatterns = [
    path('api/v1/root/fetch/', GetRootUserInfirmation.as_view()),
    path('api/v1/wife/fetch/', InsertWifeToRootTree.as_view()),
    path('api/v1/spouse/fetch/', InsertSpouseToRootTree.as_view()),

]
