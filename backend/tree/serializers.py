from rest_framework import serializers

from tree.models import MainRootUser, MainRootUserSpouse


class MainRootUserSerializer(serializers.ModelSerializer):
    """
    serialize get request about root user of tree
    """
    lastName = serializers.CharField(source='rootUser.last_name')
    firstName = serializers.CharField(source='rootUser.first_name')

    class Meta:
        model = MainRootUser
        fields = ("id", "rootUser", "buildsBy", "years",
                  'firstName', 'lastName', 'surname', 'mother_surname',
                  'date_of_birth', 'place_of_birth', 'date_of_marry', 'date_of_death')


class PartialUpdateMainRootUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainRootUser
        fields = (
            'surname', 'mother_surname',
            'date_of_birth', 'place_of_birth', 'date_of_marry'
        )


class GetWifeOrSpouseToRootTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainRootUserSpouse
        fields = (
            "name", "surname", "last_name",
            "mother_surname",
            "date_of_birth", "place_of_birth",
            "date_of_marry", "is_dead", "date_of_death",
            "email", "user"
        )


class InsertWifeOrSpouseToRootTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainRootUserSpouse
        fields = ("id", "wife",
                  "name", "surname", "last_name",
                  "mother_surname",
                  "date_of_birth", "place_of_birth",
                  "date_of_marry", "is_dead", "date_of_death",
                  "email", "user"
                  )
