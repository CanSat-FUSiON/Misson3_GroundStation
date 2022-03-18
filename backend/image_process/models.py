import uuid
from django.db import models


class ImageTestModel(models.Model):
    Rotation = models.FloatField()
    Occupancy = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created_on)

