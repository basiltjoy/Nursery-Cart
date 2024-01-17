from django.db import models

class Fertilizer(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    benefits = models.TextField()

    def __str__(self):
        return self.name