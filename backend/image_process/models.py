import uuid
from django.db import models


class ImageTestModel(models.Model):
    class Meta:
        db_table = "image_test"

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    image = models.ImageField()
