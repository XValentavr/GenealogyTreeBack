from rest_framework import serializers

from deal.models import DealWithClient


class DealSerializers(serializers.ModelSerializer):
    """
    This class creates json object from user profile table from database
    """
    document = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)

    class Meta:
        model = DealWithClient
        fields = ('date',
                  'document',
                  'context',
                  'genealog',
                  'unique')


class CreateDealSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealWithClient
        fields = ('client', 'date',
                  'document',
                  'context', 'is_published',
                  'genealog')


class UpdatePartialDealSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealWithClient
        fields = ('date',
                  'document',
                  'context', 'is_published',
                  'genealog')
