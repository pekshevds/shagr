from django.db import models

from django.contrib.auth.models import User



class Buyer(models.Model):
	
	user 					= models.OneToOneField(User, on_delete=models.PROTECT)

	first_name 				= models.CharField(max_length=150, verbose_name='Имя', blank=True)
	last_name 				= models.CharField(max_length=150, verbose_name='Фамилия', blank=True)
	phone	 				= models.CharField(max_length=150, verbose_name='Телефон', blank=True, null=True)

	address 				= models.CharField(max_length=1024, verbose_name='Адрес', blank=True)

	email 					= models.CharField(max_length=30, verbose_name='Email', blank=True)

	locality 				= models.CharField(max_length=20, verbose_name='Нас. пункт', blank=True, default='')
	street 					= models.CharField(max_length=30, verbose_name='Улица', blank=True, default='')
	house 					= models.CharField(max_length=10, verbose_name='Дом', blank=True, default='')
	apartments 				= models.CharField(max_length=10, verbose_name='Кв.', blank=True, default='')
	porch 					= models.CharField(max_length=10, verbose_name='Подъезд', blank=True, default='')
	floor 					= models.CharField(max_length=10, verbose_name='Этаж', blank=True, default='')

	def __str__(self):
		
		return self.last_name


	def save(self, *args, **kwargs):

		self.address = "{}, {}, д. {}, кв. {}, подъезд {}, этаж {}".format(self.locality, self.street, self.house, self.apartments, self.porch, self.floor)
		
		super(Buyer, self).save(*args, **kwargs)


	class Meta:
		
		verbose_name = 'Покупатель'
		verbose_name_plural = 'Покупатели'
