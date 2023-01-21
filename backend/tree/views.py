from rest_framework import authentication, permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from tree.models import MainRootUser, MainRootUserWife, MainRootUserSpouse, AnyTreeInfo
from tree.serializers import PartialUpdateOrGetMainRootUserSerializer, \
    GetWifeOrSpouseToRootTreeSerializer, InsertWifeOrSpouseToRootTreeSerializer
from tree.special_functions import add_new_params_to_request


class GetTreeRootUserInformation(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request, uuid):
        """
        Works with GET request
        :param request: all data in request
        :param uuid: user identifier
        :return: response 201 or 500
        """
        rootUser = MainRootUser.objects.filter(rootUser__id=uuid).first()
        if rootUser.buildsBy:
            treeRootUserAnyInfo = AnyTreeInfo.objects.filter(id=rootUser.anyInfo_id).first()
            serialized = PartialUpdateOrGetMainRootUserSerializer(treeRootUserAnyInfo, context={"request": request})
            if serialized.data:
                return Response(serialized.data, status=201)

        return Response('An error occurred. Bad request', status=500)


class PatchTreeRootUserInformation(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [JSONRenderer]

    @staticmethod
    def patch(request, uuid):
        """
        Represents PATCH request
        :param request: all data in request
        :param uuid: tree identifier
        :return: response 201 or 500
        """
        treeRootUser = MainRootUser.objects.filter(rootUser__id=uuid).first()
        treeRootUserAnyInfo = AnyTreeInfo.objects.filter(id=treeRootUser.anyInfo_id).first()

        if not treeRootUserAnyInfo:
            anyInfo = AnyTreeInfo.objects.create(firstName=None, surname=None, lastName=None, motherSurname=None,
                                                 dateOfBirth=None, placeOfBirth=None, dateOfMarry=None,
                                                 dateOfDeath=None, placeOfDeath=None, reasonOfDeath=None, document=None,
                                                 isPublished=False, sex='м',
                                                 isConfidential=False)

            treeRootUser.anyInfo = anyInfo
            treeRootUser.save()

        treeRootUserAnyInfo = AnyTreeInfo.objects.filter(id=treeRootUser.anyInfo_id).first()
        root_serialized = PartialUpdateOrGetMainRootUserSerializer(
            treeRootUserAnyInfo,
            data=request.data, partial=True)

        if root_serialized.is_valid():
            root_serialized.save()
            return Response("It's OK.", status=201)
        return Response('An error occurred. Bad request', status=500)


class WifeOrSpouseToRootTree(RetrieveUpdateDestroyAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GetWifeOrSpouseToRootTreeSerializer

    def get_queryset(self):
        if 'wife' in self.request.data:
            return MainRootUserWife.objects.filter(spouse__user__uid=self.kwargs['uuid'])
        elif 'spouse' in self.request.data:
            return MainRootUserSpouse.objects.filter(wife__user__uid=self.kwargs['uuid'])


class InsertWifeOrSpouseToRootTree(CreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = InsertWifeOrSpouseToRootTreeSerializer

    def create(self, request, *args, **kwargs):
        request = add_new_params_to_request(request, kwargs['uuid'])
        if 'is_you' in request.data:
            return Response({"Це ви"}, status=404)
        super().create(request, *args, **kwargs)
        if request.data['spouse'] is not None:
            return Response(InsertWifeOrSpouseToRootTreeSerializer(
                MainRootUserWife.objects.filter(spouse__user__uid=self.kwargs['uuid']).first()).data, status=201)
        elif request.data['wife'] is not None:
            return Response(InsertWifeOrSpouseToRootTreeSerializer(
                MainRootUserSpouse.objects.filter(wife__user__uid=self.kwargs['uuid']).first()).data, status=201)
