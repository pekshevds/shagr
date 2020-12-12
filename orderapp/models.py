from django.db import models

from authapp.models import Buyer
from catalogapp.models import Good

from shagr.core import get_uuid4
# Create your models here.

class Order(models.Model):
	
	buyer = models.ForeignKey(Buyer, verbose_name="Покупатель", on_delete=models.PROTECT)
	date = models.DateTimeField(verbose_name="Дата", auto_now_add=True)
	total = models.DecimalField(verbose_name='Сумма заказа', default=0, max_digits=15, decimal_places=2)
	comment = models.CharField(max_length=1024, verbose_name="Комментарий", null=True, blank=True)
	uid_1c = models.SlugField(max_length=36, verbose_name='Идентификатор в 1С', default="", null=True, blank=True)

	def __str__(self):
		return str(self.id) + ' от ' + str(self.date)

	def save(self, *args, **kwargs):
		
		if not self.uid_1c:
			self.uid_1c = get_uuid4()        

		super(Order, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'

class OrderItem(models.Model):
	
	order = models.ForeignKey(Order, verbose_name='Номенклатура', on_delete=models.CASCADE)
	good = models.ForeignKey(Good, verbose_name='Номенклатура', on_delete=models.PROTECT)
	quant = models.DecimalField(verbose_name='Количество', default=0, max_digits=15, decimal_places=3)
	price = models.DecimalField(verbose_name='Цена', default=0, max_digits=15, decimal_places=2)
	total = models.DecimalField(verbose_name='Сумма', default=0, max_digits=15, decimal_places=2)

	class Meta:
		verbose_name = 'Строка заказа'
		verbose_name_plural = 'Строки заказа'