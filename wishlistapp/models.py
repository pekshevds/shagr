from django.db import models
from authapp.models import Buyer
from catalogapp.models import Good

# Create your models here.
class Item(models.Model):
	buyer = models.ForeignKey(Buyer, verbose_name="Покупатель", on_delete=models.PROTECT,)
	good = models.ForeignKey(Good, verbose_name="Товар", on_delete=models.PROTECT,)    
    
	class Meta:
		verbose_name = 'Записи'
		verbose_name_plural = 'Избранное'