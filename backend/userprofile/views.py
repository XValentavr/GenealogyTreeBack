from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework import authentication, permissions

from authentication.models import UserAccount
from userprofile.models import UserProfile
from .serializers import UserSerizalier


# Create your views here.

class UserOperation(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request, uuid):
        """
        this function creates GET request to get info abount user profile
        :param request: all request data
        :param uuid: user unique identifier
        :return: json object from got data
        """
        queryset = UserProfile.objects.select_related('user').filter(user__uid=uuid)
        serializer = UserSerizalier(queryset, many=True, context={"request": request})
        return Response(serializer.data, status=HTTP_200_OK)

    @staticmethod
    def patch(request, uuid):
        profile = UserProfile.objects.filter(user__uid=uuid).first()
        user = UserAccount.objects.filter(uid=uuid).first()
        json = request.data
        user.username = json['username']
        user.lastname = json['last_name']
        profile.avatar = json['avatar']
        profile.telegram = json['telegram']
        profile.facebook = json['facebook']
        profile.whatsapp = json['whatsapp']
        profile.linkedin = json['linkedin']
        profile.date_of_birth = json['date_of_birth']

        profile.save()
        user.save()
        return Response("It's OK.", status=HTTP_200_OK)
