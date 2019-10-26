from django.db import models
from uuid import uuid4

from data.models import *
# Create your models here.

class AnimalType(models.Model):
    uuid=models.UUIDField(blank=False, default=uuid4, primary_key=True)
    type = models.CharField(max_length=255, blank=False, unique=True)

class Animal(models.Model):
    uuid=models.UUIDField(blank=False, default=uuid4, primary_key=True)
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True, null=True)
    id_type = models.ForeignKey(AnimalType, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, default="В поиске")
    photo_path = models.CharField(max_length=255)
    @classmethod
    def create_animal;(cls, name, type_name, status):
        

class AnimalAdoption(models.Model):
    uuid=models.UUIDField(blank=False, default=uuid4, primary_key=True)
    user = models.ManyToManyField(User)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

    

class AnimalPhoto(models.Model):
    uuid=models.UUIDField(blank=False, default=uuid4, primary_key=True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    photo = models.CharField(max_length=255)
