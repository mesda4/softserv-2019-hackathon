from django.db import models
from animals.models import Animal


class NeedType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class OrpanageNeed(models.Model):
    name = models.CharField(max_length=200)
    # id_type = models.ManyToManyField(NeedType)
    id_type = models.ForeignKey(NeedType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# class Need(models.Model):
#     name = models.CharField(max_length=200)
#     id_type = models.ForeignKey(NeedType, on_delete=models.CASCADE)
#     id_animal = models.ForeignKey(Animal, on_delete=models.CASCADE, null=True, blank=True)
#
#     def __str__(self):
#         return self.name

class AnimalNeed(models.Model):
    name = models.CharField(max_length=200)
    # id_type = models.ManyToManyField(NeedType)
    id_animal = models.ForeignKey(Animal, on_delete=models.CASCADE, null=True, blank=True)
    id_type = models.ForeignKey(NeedType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
