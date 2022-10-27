from django.urls import path

from tree.views import GetRootUserInfirmation, WifeOrSpouseToRootTree, InsertWifeOrSpouseToRootTree

urlpatterns = [
    path('api/v1/fetch/root', GetRootUserInfirmation.as_view()),
    path('api/v1/fetch/<int:pk>', WifeOrSpouseToRootTree.as_view()),
    path('api/v1/fetch/', InsertWifeOrSpouseToRootTree.as_view()),

]
