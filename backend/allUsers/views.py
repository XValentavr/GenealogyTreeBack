from rest_framework import authentication, permissions
from rest_framework.generics import ListAPIView

from allUsers.serializers import GetAllUsers
from authentication.models import UserAccount


class GetAllUsersToCheckIsGenealogist(ListAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GetAllUsers
    queryset = UserAccount.objects.all()
