from django.db import models
from catalogapp.models import Good
from django.db.models import Sum

from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
	user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.PROTECT, null=True, blank=True)
	

	def get_items(self):
		return CartItem.objects.filter(cart=self)


	def get_items_count(self):
		return (CartItem.objects.filter(cart=self).aggregate(Sum('quant'))['quant__sum'])

	def get_quant(self):
		quant = 0
		
		for item in CartItem.objects.filter(cart=self):
			quant += item.quant

		return quant


	def get_amount(self):
		amount = 0
		
		for item in CartItem.objects.filter(cart=self):
			amount += item.get_amount()

		return amount


	def clear(self):
		try:
			CartItem.objects.filter(cart=self).delete()
		except:
			return False
		return True


	class Meta:
		verbose_name = 'Корзина'
		verbose_name_plural = 'Корзина'


class CartItem(models.Model):
	cart = models.ForeignKey(Cart, verbose_name="Корзина", on_delete=models.CASCADE)
	good = models.ForeignKey(Good, verbose_name="Товар", on_delete=models.PROTECT)
	quant = models.PositiveIntegerField(verbose_name='Количество', default=1)
    
	def get_amount(self):
		return self.good.price * self.quant

	def __str__(self):
		return self.good.name

	class Meta:
		verbose_name = 'Элементы корзины'
		verbose_name_plural = 'Элемент корзины'