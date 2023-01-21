from django.urls import path

from genealogistBuildsTree.views import GetBuildTreeBySuperGenealogist, BuildTreeByGenealogist, \
    GetBuildTreeByGenealogist

urlpatterns = [
    path('api/v1/fetch/', GetBuildTreeBySuperGenealogist.as_view()),
    path('api/v1/fetch/(?P<status>\w+)/', GetBuildTreeBySuperGenealogist.as_view()),
    path('<pk>/api/v1/fetch/', BuildTreeByGenealogist.as_view()),
    path('<genealogist>/api/v1/fetch/genealogist/', GetBuildTreeByGenealogist.as_view()),

]
