from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework import authentication, permissions

from authentication.models import UserAccount
from dtos.profile.update_profile_dto import UpdateProfileDTO
from dtos.user.user_dto import UserUpdateDto
from userprofile.models import UserProfile
from userprofile.serializers import UserSerializer, PartialUpdateUserSerializer, \
    PartialUpdateUserProfileSerializer


class UserOperation(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request, uuid):
        """
        this function creates GET request to get info about user profile
        :param request: all request data
        :param uuid: user unique identifier
        :return: json object from got data
        """
        queryset = UserProfile.objects.filter(user__id=uuid)
        serializer = UserSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data, status=HTTP_200_OK)

    @staticmethod
    def patch(request, uuid):
        """
        This function represents patch request
        :param request: all data in request
        :param uuid: unique user identifier
        :return: Response
        """
        # can be updated
        user_update_dto = UserUpdateDto(**request.data).dict(exclude_none=True)

        user = PartialUpdateUserSerializer(UserAccount.objects.filter(uid=uuid).first(), user_update_dto,
                                           partial=True)

        update_profile_dto = UpdateProfileDTO(**request.data).dict(exclude_none=True)
        profile = PartialUpdateUserProfileSerializer(UserProfile.objects.filter(user__uid=uuid).first(),
                                                     data=update_profile_dto, partial=True)
        if user.is_valid() and profile.is_valid():
            user.save()
            profile.save()
            return Response("It's OK.", status=201)
        return Response(status=500)
