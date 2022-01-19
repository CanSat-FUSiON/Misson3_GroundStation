from rest_framework import serializers

from .models import ImageTestModel


class ImageTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageTestModel
        fields = "__all__"
