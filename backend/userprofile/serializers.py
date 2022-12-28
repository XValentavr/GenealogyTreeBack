from rest_framework import serializers

from authentication.models import UserAccount
from userprofile.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    """
    This class creates json object from user profile table from database
    """
    photoUrl = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    userName = serializers.CharField(source='user.username')
    lastName = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')
    sex = serializers.CharField(source='user.sex')
    isGenealogist = serializers.BooleanField(source='user.is_genealogist')
    isSuperuser = serializers.BooleanField(source='user.is_superuser')

    class Meta:
        model = UserProfile
        fields = ('userName',
                  'lastName',
                  'avatar',
                  'telegram',
                  'facebook',
                  'linkedin',
                  'whatsapp',
                  'twitter',
                  'photoUrl',
                  'email',
                  'sex',
                  'isGenealogist',
                  'isSuperuser',)


class PartialUpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('userName',
                  'lastName',
                  'firstName',
                  'email')


class PartialUpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('avatar',
                  'telegram',
                  'facebook',
                  'linkedin',
                  'whatsapp',
                  'twitter',
                  'avatar')
