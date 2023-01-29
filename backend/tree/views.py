from rest_framework import authentication, permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from dtos.tree.pathTreeRootUserDTO import PatchTreeRootDTO
from tree.models import MainRootUser, AnyTreeInfo, MainRootUserWife, MainRootUserSpouse, FemaleLine, MaleLine
from tree.serializers import PartialUpdateOrGetOrPostMainRootUserSerializer, \
    GetWifeOrSpouseToRootTreeSerializer, InsertWifeOrSpouseToRootTreeSerializer
from helpers.enums.sex_enum import SexEnum
from helpers.special.special_functions import add_new_params_to_request
from services.CRUD.tree.create_initial_anyinfo import create_initial_any_info
from services.CRUD.tree.create_male_or_female_line import create_male_of_female_line


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
            serialized = PartialUpdateOrGetOrPostMainRootUserSerializer(treeRootUserAnyInfo,
                                                                        context={"request": request})
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
        anyInfo = create_initial_any_info(treeRootUser, treeRootUserAnyInfo)

        patch_data_dto = PatchTreeRootDTO(**request.data).dict(exclude_none=True)

        root_serialized = PartialUpdateOrGetOrPostMainRootUserSerializer(
            treeRootUserAnyInfo if treeRootUserAnyInfo else anyInfo,
            data=patch_data_dto, partial=True)

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


class CreateMaleOrFemaleLine(CreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        postTreeLineDTO = PatchTreeRootDTO(**request.data).dict(exclude_none=True)
        if request.data.get('sex') == SexEnum.FEMALE.value:
            femaleLineAnyInfo = PartialUpdateOrGetOrPostMainRootUserSerializer(data=postTreeLineDTO)
            return create_male_of_female_line(uuid=self.kwargs['uuid'], lineInfo=femaleLineAnyInfo, model=FemaleLine)

        if request.data.get('sex') == SexEnum.MALE.MALE:
            maleLineAnyInfo = PartialUpdateOrGetOrPostMainRootUserSerializer(data=postTreeLineDTO)
            return create_male_of_female_line(uuid=self.kwargs['uuid'], lineInfo=maleLineAnyInfo, model=MaleLine)
        return Response(status=HTTP_400_BAD_REQUEST)
