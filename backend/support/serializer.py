from rest_framework import serializers

from support.models import Support


class TechSupportSerializer(serializers.ModelSerializer):
    """
    Represents POST request to insert tech data
    """

    class Meta:
        model = Support
        fields = "__all__"
