from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from genealogistBuildsTree.models import GenealogistBuildsTree
from genealogistBuildsTree.serializers import GetGenealogistBuildsTreeSerializers, \
    CreateGenealogistBuildsTreeSerializers, ChangeOrDeleteGenealogistBuildsTreeSerializers
from tree.models import MainRootUser


class GetBuildTreeByGenealogist(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request):
        """
        this function creates GET request to get all ordering to create tree
        :param request: all request data
        :return: json object from got data
        """
        queryset = GenealogistBuildsTree.objects.all()
        serializer = GetGenealogistBuildsTreeSerializers(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    @staticmethod
    def post(request):
        """
        this function creates POST request to get all ordering to create tree
        :param request: all request data
        :return: json object from got data
        """
        serializer = CreateGenealogistBuildsTreeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            buildsBy = GenealogistBuildsTree.objects.filter(client=request.data.get("client")).first()

            setBuildsBy = MainRootUser.objects.filter(rootUser=request.data.get("client")).first()
            setBuildsBy.buildsBy = buildsBy
            setBuildsBy.save()

            return Response(status=HTTP_200_OK)
        return Response(status=HTTP_400_BAD_REQUEST)


class BuildTreeByGenealogist(RetrieveUpdateDestroyAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]
    serializer_class = ChangeOrDeleteGenealogistBuildsTreeSerializers
    queryset = GenealogistBuildsTree.objects.all()
