from django.urls import path

from tree.views import GetRootUserInformation, WifeOrSpouseToRootTree, InsertWifeOrSpouseToRootTree

urlpatterns = [
    path('api/v1/fetch/root', GetRootUserInformation.as_view()),
    path('api/v1/fetch/<int:pk>', WifeOrSpouseToRootTree.as_view()),
    path('api/v1/fetch/', InsertWifeOrSpouseToRootTree.as_view()),

]
