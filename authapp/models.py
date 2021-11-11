from django.db import models

from django.contrib.auth.models import User



class Buyer(models.Model):
	
	user 					= models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.PROTECT)

	first_name 				= models.CharField(max_length=150, verbose_name='Имя', blank=False)
	last_name 				= models.CharField(max_length=150, verbose_name='Фамилия', blank=True)
	middle_name 			= models.CharField(max_length=150, verbose_name='Отчество', blank=True)
	phone	 				= models.CharField(max_length=150, verbose_name='Телефон', blank=True, null=True)

	address 				= models.CharField(max_length=1024, verbose_name='Адрес', blank=True, default='')

	email 					= models.CharField(max_length=30, verbose_name='Email', blank=True)

	zipcode	 				= models.CharField(max_length=12, verbose_name='Индекс', blank=True, default='')
	locality 				= models.CharField(max_length=20, verbose_name='Нас. пункт', blank=True, default='')
	street 					= models.CharField(max_length=30, verbose_name='Улица', blank=True, default='')
	house 					= models.CharField(max_length=10, verbose_name='Дом', blank=True, default='')
	apartments 				= models.CharField(max_length=10, verbose_name='Кв.', blank=True, default='')
	porch 					= models.CharField(max_length=10, verbose_name='Подъезд', blank=True, default='')
	floor 					= models.CharField(max_length=10, verbose_name='Этаж', blank=True, default='')

	def __str__(self):
		
		return self.first_name + " " + self.last_name


	def save(self, *args, **kwargs):

		self.address = "{}{}{}{}{}{}{}".format(
				(self.zipcode) if self.zipcode else '',
				(', ' +  self.locality) if self.locality else '',
				(', ' +  self.street) if self.street else '',
				(', д. ' +  self.house) if self.house else '',
				(', кв. ' + self.apartments) if self.apartments else '',
				(', подъезд ' + self.porch) if self.porch else '',
				(', этаж' + self.floor) if self.floor else ''
			)
		
		super(Buyer, self).save(*args, **kwargs)


	class Meta:
		
		verbose_name = 'Покупатель'
		verbose_name_plural = 'Покупатели'
