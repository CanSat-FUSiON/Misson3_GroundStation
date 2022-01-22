from rest_framework import serializers

from .models import ImageTestModel


class ImageTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageTestModel
        fields = "__all__"


<<<<<<< HEAD
class EnvironmentSerializer(serializers.Serializer):

    temparature = serializers.DecimalField(max_digits=10, decimal_places=5)
    accelaration_x = serializers.DecimalField(max_digits=5, decimal_places=2)
=======
class ImageCaptureSerializer(serializers.Serializer):
    pass
>>>>>>> f312ff2 (add comments)
