from rest_framework import authentication, permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models import UserAccount
from tree.models import MainRootUser, MainRootUserWife, MainRootUserSpouse
from tree.serializers import MainRootUserSerializer, PartialUpdateMainRootUserSerializer, \
    GetWifeOrSpouseToRootTreeSerializer, InsertWifeOrSpouseToRootTreeSerializer
from tree.special_functions import add_new_params_to_request
from userprofile.serializers import PartialUpdateUserSerializer


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
        root_user = MainRootUser.objects.filter(rootUser__id=uuid).all()
        for user in root_user:
            if user.buildsBy:
                serialized = MainRootUserSerializer(user, context={"request": request})
                if serialized:
                    return Response(serialized.data, status=201)
        serialized = MainRootUserSerializer(root_user[0], context={"request": request})
        if serialized:
            return Response(serialized.data, status=201)

        return Response('An error occurred. Bad request', status=500)


class PatchTreeRootUserInformation(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def patch(request, uuid):
        """
        Represents PATCH request
        :param request: all data in request
        :param uuid: tree identifier
        :return: response 201 or 500
        """
        print(request.data)
        treeRootUser = MainRootUser.objects.filter(id=uuid).first()
        root_serialized = PartialUpdateMainRootUserSerializer(
            treeRootUser,
            data=request.data, partial=True)
        user = UserAccount.objects.filter(id=treeRootUser.rootUser.id).first()

        user_serialized = PartialUpdateUserSerializer(user, data=request.data,
                                                      partial=True)
        if user_serialized.is_valid() and root_serialized.is_valid():
            user_serialized.save()
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
