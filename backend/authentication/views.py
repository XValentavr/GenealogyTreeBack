from django.views.generic import TemplateView
from rest_framework import authentication, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from authentication.models import UserAccount


# Create your views here.

class RegisterView(TemplateView):
    template_name = 'authentication/base.html'


class ResetPassword(TemplateView):
    template_name = 'authentication/reset_password.html'


class SetNewPassword(TemplateView):
    template_name = 'authentication/set_new_password.html'


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
