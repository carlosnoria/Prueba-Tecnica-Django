from django.db import models

class Ciudad(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ["name"]

class Usuario(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    document = models.CharField(max_length=10, unique=True)

class Tienda(models.Model):
    name = models.CharField(max_length=30)
    city = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    users = models.ManyToManyField(Usuario)

    class Meta:
        ordering = ["city", "name"]
