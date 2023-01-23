from rest_framework import serializers

from tree.models import MainRootUser, MainRootUserSpouse, AnyTreeInfo


class MainOrFemaleOrMaleLinesSerializer(serializers.ModelSerializer):
    """
    serialize get request about root user of tree
    """
    anyInfo = serializers.RelatedField(read_only=True)

    def to_representation(self, instance):
        return PartialUpdateOrGetOrPostMainRootUserSerializer(instance).data

    class Meta:
        model = MainRootUser
        fields = ("id", "rootUser", "buildsBy", "anyInfo")


class PartialUpdateOrGetOrPostMainRootUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnyTreeInfo
        fields = ('id', 'firstName', 'lastName',
                  'surname', 'motherSurname',
                  'dateOfBirth', 'placeOfBirth', 'dateOfMarry',
                  'dateOfDeath', 'isConfidential', 'placeOfDeath',
                  'reasonOfDeath', 'sex'
                  )


class GetWifeOrSpouseToRootTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainRootUserSpouse
        fields = (
            "anyInfo__surname", "anyInfo__lastName",
            "anyInfo__motherSurname",
            "anyInfo__dateOfBirth", "anyInfo__placeOfBirth",
            "anyInfo__dateOfMarry", "anyInfo__isDead", "anyInfo__dateOfDeath",
            "anyInfo__email"
        )


class InsertWifeOrSpouseToRootTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainRootUserSpouse
        fields = ("id", "wife",
                  "anyInfo__firstName", "anyInfo__surname", "anyInfo__lastName",
                  "anyInfo__motherSurname",
                  "anyInfo__dateOfBirth", "anyInfo__placeOfBirth",
                  "anyInfo__dateOfMarry", "anyInfo__isDead", "anyInfo__dateOfDeath",
                  "anyInfo__email", "anyInfo__user"
                  )
