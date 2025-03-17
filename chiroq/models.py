from django.db import models


# Create your models here.

class Chiroq(models.Model):
    brand = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    quantity = models.PositiveIntegerField()
    vatt_kuchi = models.PositiveIntegerField()
    color = models.CharField(max_length=16)
    image = models.ImageField(upload_to='dorilar/', blank=True, null=True)

    class Mete:
        verbose_name = 'Chiroq'

    def __str__(self):
        return self.brand
