from django.db import models


class image(models.Model):
    image_name = models.CharField(verbose_name='image_name', max_length=32)
    image_type = models.CharField(verbose_name='image_type', max_length=32)
    image = models.FileField(verbose_name='image')
