from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    #id = models.AutoField(primary_key=True)
    name = models.CharField('Модель', max_length=50, default='')
    material = models.CharField('Материал', max_length=50, default='')
    mattress = models.CharField('Матрац', max_length=50, default='')
    price = models.IntegerField('Цена', default='0')

    def __str__(self):
        return '%s %s %s %d' %(self.name, self.material, self.mattress, self.price)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'