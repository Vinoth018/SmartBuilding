# myapp/models.py
from django.db import models

class Building(models.Model):
    image_url = models.URLField(max_length=200)
    building_name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return self.building_name
