from rest_framework import serializers

from genealogistBuildsTree.models import GenealogistBuildsTree


class GetGenealogistBuildsTreeSerializers(serializers.ModelSerializer):
    userName = serializers.CharField(source='client.username')
    lastName = serializers.CharField(source='client.last_name')
    email = serializers.CharField(source='client.email')
    genealogistName = serializers.CharField(source='genealogist.username', allow_null=True)
    genealogistLastName = serializers.CharField(source='genealogist.last_name', allow_null=True)
    rootTreeId = serializers.CharField(source='client.id')

    class Meta:
        model = GenealogistBuildsTree
        fields = ('id', 'userName', 'lastName',
                  "email", 'genealogistName', 'genealogistLastName', "status", "colorCode", 'rootTreeId')


class CreateGenealogistBuildsTreeSerializers(serializers.ModelSerializer):
    class Meta:
        model = GenealogistBuildsTree
        fields = ('client',)


class ChangeOrDeleteGenealogistBuildsTreeSerializers(serializers.ModelSerializer):
    class Meta:
        model = GenealogistBuildsTree
        fields = ('genealogist', "colorCode", "status")
