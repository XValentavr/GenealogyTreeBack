from django.urls import path

from genealogistBuildsTree.views import GetBuildTreeByGenealogist, BuildTreeByGenealogist

urlpatterns = [
    path('api/v1/fetch/', GetBuildTreeByGenealogist.as_view()),
    path('<pk>/api/v1/fetch/', BuildTreeByGenealogist.as_view()),

]
