from rest_framework import authentication, permissions
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListAPIView
from authentication.models import UserAccount
from authentication.serializers import GetUserUUID


class GetUserAfterAuth(ListAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GetUserUUID

    def get_queryset(self):
        return UserAccount.objects.filter(id=Token.objects.get(key=self.request.auth.key).user_id)
