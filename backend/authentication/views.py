from django.views.generic import TemplateView
from rest_framework import authentication, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from authentication.models import UserAccount



class GetUserAfterAuth(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request):
        """
        this function creates GET request to get info abount user profile
        :param request: all request data (body, headers)
        :return: json object from got data
        """
        user_id = Token.objects.get(key=request.auth.key).user_id
        user = UserAccount.objects.filter(id=user_id).first()
        return Response({'uuid': user.uid}, status=HTTP_200_OK)


class GetUserUUIDToChangeDeal(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request):
        """
        this function creates GET request to get user uuid
        :param request: all request data (body, headers)
        :return: json object from got data
        """
        client = UserAccount.objects.filter(email=request.query_params.get('useremail')).first().uid
        return Response({'uid': client}, status=HTTP_200_OK)
