from django.db import models
from django.utils.text import slugify
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
import core.helper as hlp

class City(models.Model):
    name = models.CharField(max_length=30, verbose_name="Şehir")

    class Meta:
        db_table = "city"

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=30, verbose_name="İlçe")
    city = models.ForeignKey(City, on_delete=models.PROTECT)

    class Meta:
        db_table = "district"

    def __str__(self):
        return self.name
