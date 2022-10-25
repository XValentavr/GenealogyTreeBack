from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework import authentication, permissions

from authentication.models import UserAccount
from userprofile.models import UserProfile
from .serializers import UserSerizalier, PartialUpdateUserSerializer, PartialUpdateUserProfileSerializer


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
        """
        This function represents patch request
        :param request: all data in request
        :param uuid: unique user udentifier
        :return: Response
        """
        # can be updated
        user = PartialUpdateUserSerializer(UserAccount.objects.filter(uid=uuid).first(), data=request.data,
                                           partial=True)
        profile = PartialUpdateUserProfileSerializer(UserProfile.objects.filter(user__uid=uuid).first(),
                                                     data=request.data, partial=True)
        if user.is_valid() and profile.is_valid():
            user.save()
            profile.save()
            return Response("It's OK.", status=201)
        return Response(status=500)
