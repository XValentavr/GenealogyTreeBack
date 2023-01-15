from rest_framework import serializers

from authentication.models import UserAccount


class GetAllUsers(serializers.ModelSerializer):
    userName = serializers.CharField(source='username')
    lastName = serializers.CharField(source='last_name')
    isSuperuser = serializers.BooleanField(source='is_superuser')

    class Meta:
        model = UserAccount
        fields = ('id', 'userName', 'lastName', 'email', 'isGenealogist', 'isSuperuser')
