from rest_framework import serializers

from tree.models import MainRootUser


class MainRootUserSerializer(serializers.ModelSerializer):
    """
    resialize get request abount root user of tree
    """
    lastname = serializers.CharField(source='user.last_name')
    first_name = serializers.CharField(source='user.first_name')

    class Meta:
        model = MainRootUser
        fields = (
            'first_name', 'lastname', 'surname', 'mother_surname',
            'date_of_birth', 'place_of_birth', 'date_of_marry')


class PartialUpdateMainRootUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainRootUser
        fields = (
            'surname', 'mother_surname',
            'date_of_birth', 'place_of_birth', 'date_of_marry'
        )
