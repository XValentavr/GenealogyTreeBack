from django.urls import path

from tree.views import GetTreeRootUserInformation, WifeOrSpouseToRootTree, InsertWifeOrSpouseToRootTree, \
    PatchTreeRootUserInformation, CreateMaleOrFemaleLine

urlpatterns = [
    path('api/v1/fetch/root', GetTreeRootUserInformation.as_view()),
    path('api/v1/fetch/tree', PatchTreeRootUserInformation.as_view()),

    path('api/v1/fetch/<int:pk>', WifeOrSpouseToRootTree.as_view()),
    path('api/v1/fetch/', InsertWifeOrSpouseToRootTree.as_view()),
    path('api/v1/fetch/line', CreateMaleOrFemaleLine.as_view()),

]
