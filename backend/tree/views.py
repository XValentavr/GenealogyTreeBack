from rest_framework import authentication, permissions
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models import UserAccount
from tree.models import MainRootUser
from tree.serializers import MainRootUserSerializer, PartialUpdateMainRootUserSerializer, InsertWifeToRootTreeSerializer
from userprofile.serializers import PartialUpdateUserSerializer


class GetRootUserInfirmation(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    @staticmethod
    def get(request, uuid):
        """
        Works with GET request
        :param request: all data in request
        :param uuid: user identifier
        :return: response 201 or 500
        """
        root_user = MainRootUser.objects.select_related('user').filter(user__uid=uuid).first()
        serialized = MainRootUserSerializer(root_user, context={"request": request})
        if serialized:
            return Response(serialized.data, status=201)
        return Response('An error occured. Bad request', status=500)

    @staticmethod
    def patch(request, uuid):
        """
        Represents PATCH request
        :param request: all data in request
        :param uuid: user iidentifier
        :return: response 201 or 500
        """
        user = UserAccount.objects.filter(uid=uuid).first()
        user_serialized = PartialUpdateUserSerializer(user, data=request.data,
                                                      partial=True)

        root_serialized = PartialUpdateMainRootUserSerializer(
            MainRootUser.objects.filter(user__uid=uuid).first(),
            data=request.data, partial=True)

        if user_serialized.is_valid() and root_serialized.is_valid():
            user_serialized.save()
            root_serialized.save()
            return Response("It's OK.", status=201)
        return Response('An error occured. Bad request', status=500)


class InsertWifeToRootTree(CreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = InsertWifeToRootTreeSerializer

    def create(self, request, *args, **kwargs):
        request.data['spouse'] = MainRootUser.objects.filter(user__uid=kwargs['uuid']).first().pk

        if 'email' in request.data:
            user = UserAccount.objects.filter(email=request.data['email']).first().pk
            if not user:
                user = ''
            request.data['user'] = user

        super().create(request, *args, **kwargs)
        return Response(status=200)


class InsertSpouseToRootTree(CreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = InsertWifeToRootTreeSerializer

    def create(self, request, *args, **kwargs):
        request.data['wife'] = MainRootUser.objects.filter(user__uid=kwargs['uuid']).first().pk

        if 'email' in request.data:
            user = UserAccount.objects.filter(email=request.data['email']).first().pk
            if not user:
                user = ''
            request.data['user'] = user

        super().create(request, *args, **kwargs)
        return Response(status=200)
