from django.contrib import admin

from .models import ImageTestModel


@admin.register(ImageTestModel)
class ImageTestModelAdmin(admin.ModelAdmin):
    pass
