from rest_framework import serializers

from userprofile.models import UserProfile


class UserSerizalier(serializers.ModelSerializer):
    """
    This class creates json object from user profile table from database
    """
    photo_url = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    user_name = serializers.CharField(source='user.username')
    lastname = serializers.CharField(source='user.last_name')

    class Meta:
        model = UserProfile
        fields = ('user_name',
                  'lastname',
                  'date_of_birth',
                  'avatar',
                  'telegram',
                  'facebook',
                  'linkedin',
                  'whatsapp',
                  'twitter',
                  'photo_url')
