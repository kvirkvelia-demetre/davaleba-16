from django.db import models

class Product(models.Model):
    name = models.CharField()
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

