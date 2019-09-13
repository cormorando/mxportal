from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, default='')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.id)])
