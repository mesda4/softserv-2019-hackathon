from django.db import models

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