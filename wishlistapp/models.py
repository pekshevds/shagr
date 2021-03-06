from django.db import models
from catalogapp.models import Good

from django.contrib.auth.models import User

# Create your models here.
class WishList(models.Model):
	user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.PROTECT, null=True, blank=True)
	

	def get_items(self):
		return WishListItem.objects.filter(wishlist=self)


	def get_items_count(self):
		return len(WishListItem.objects.filter(wishlist=self))


	class Meta:
		verbose_name = 'Избранное'
		verbose_name_plural = 'Избранное'	


class WishListItem(models.Model):
	wishlist = models.ForeignKey(WishList, verbose_name="Избранное", on_delete=models.CASCADE)
	good = models.ForeignKey(Good, verbose_name="Товар", on_delete=models.PROTECT)

    
	def __str__(self):
		return self.good.name


	class Meta:
		verbose_name = 'Записи избранного'
		verbose_name_plural = 'Запись избранного'