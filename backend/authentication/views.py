from rest_framework import authentication, permissions
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListAPIView
from authentication.models import UserAccount
from authentication.serializers import GetUserUUIDToChangeDealSerializer


class GetUserAfterAuth(ListAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GetUserUUIDToChangeDealSerializer

    def get_queryset(self):
        return UserAccount.objects.filter(id=Token.objects.get(key=self.request.auth.key).user_id)


class GetUserUUIDToChangeDeal(ListAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GetUserUUIDToChangeDealSerializer

    def get_queryset(self):
        return UserAccount.objects.filter(email=self.request.query_params.get('useremail'))
