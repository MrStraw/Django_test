from django.db import models


class TestImagesModel(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField()
