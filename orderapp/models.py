from decimal import Decimal
from django.db import models


from authapp.models import Buyer
from catalogapp.models import Good

from shagr.core import get_uuid4
# Create your models here.

DEFAULT_PAYMENT_STATUS = 'NP'
PAYMENT_STATUSES = (
	(DEFAULT_PAYMENT_STATUS, 'Ожидает оплаты'),
	('PP', 'Частично оплачен'),
	('AP', 'Оплачен полностью'),    
	)

DEFAULT_DELIVERY_STATUS = 'AW'
DELIVERY_STATUSES = (
	(DEFAULT_DELIVERY_STATUS, 'Ожидает подтверждения'),#Собирается	
	('GT', 'Собирается'),#Собирается
	('TF', 'Передан'),#Передан на доставку в ТК
	('DL', 'Доставлен'),#Передан заказчику
	('RT', 'Вернулся'),#Вернулся отправителю
	)

class Order(models.Model):
		
	buyer = models.ForeignKey(Buyer, verbose_name="Покупатель", on_delete=models.PROTECT, null=True, blank=True)
	date = models.DateTimeField(verbose_name="Дата", auto_now_add=True)
	total = models.DecimalField(verbose_name="Сумма заказа", default=0, max_digits=15, decimal_places=2)
	comment = models.CharField(max_length=1024, verbose_name="Комментарий", null=True, blank=True)
	uid_1c = models.SlugField(max_length=36, verbose_name="Идентификатор в 1С", default="", null=True, blank=True)
	payment_status = models.CharField(max_length=2, verbose_name="Состояние оплаты", 
										choices=PAYMENT_STATUSES, default=DEFAULT_PAYMENT_STATUS)
	delivery_status = models.CharField(max_length=2, verbose_name="Состояние доставки", 
										choices=DELIVERY_STATUSES, default=DEFAULT_DELIVERY_STATUS)

	weight = models.DecimalField(verbose_name='Вес, кг', default=0, max_digits=15, decimal_places=3)
	volume = models.DecimalField(verbose_name='Объем, м3', default=0, max_digits=15, decimal_places=5)

	def __str__(self):
		return str(self.id) + ' от ' + self.date.strftime("%d.%m.%Y")


	def get_items(self):
		return OrderItem.objects.filter(order=self)


	def get_items_count(self):
		return len(OrderItem.objects.filter(order=self))	


	def save(self, *args, **kwargs):
		
		if not self.uid_1c:
			self.uid_1c = get_uuid4()        

		self.total = 0
		items = OrderItem.objects.filter(order=self)
		
		result = items.aggregate(models.Sum('total'))		
		if result['total__sum']:
			self.total = result['total__sum']

		result = items.aggregate(models.Sum('weight'))		
		if result['weight__sum']:
			self.weight = result['weight__sum']

		result = items.aggregate(models.Sum('volume'))		
		if result['volume__sum']:
			self.volume = result['volume__sum']

		super(Order, self).save(*args, **kwargs)


	def display_current_payment_status(self):
		return dict(PAYMENT_STATUSES)[self.payment_status]


	def display_current_delivery_status(self):
		return dict(DELIVERY_STATUSES)[self.delivery_status]


	class Meta:
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'

class OrderItem(models.Model):
	
	order = models.ForeignKey(Order, verbose_name='Номенклатура', on_delete=models.CASCADE)
	good = models.ForeignKey(Good, verbose_name='Номенклатура', on_delete=models.PROTECT)
	quant = models.PositiveIntegerField(verbose_name='Количество', default=1)
	price = models.DecimalField(verbose_name='Цена', default=0, max_digits=15, decimal_places=2)
	discount = models.DecimalField(verbose_name='Скидка, %', default=0, max_digits=15, decimal_places=2)
	total = models.DecimalField(verbose_name='Сумма', default=0, max_digits=15, decimal_places=2)

	weight = models.DecimalField(verbose_name='Вес, кг', default=0, max_digits=15, decimal_places=3)
	volume = models.DecimalField(verbose_name='Объем, м3', default=0, max_digits=15, decimal_places=5)

	def save(self, *args, **kwargs):
		
		if self.order.payment_status == DEFAULT_PAYMENT_STATUS and self.order.delivery_status == DEFAULT_DELIVERY_STATUS:
			self.price = self.good.price

		self.total = self.price * self.quant
		self.weight = self.good.weight * self.quant
		self.volume = self.good.volume * self.quant

		super(OrderItem, self).save(*args, **kwargs)


	class Meta:
		verbose_name = 'Строка заказа'
		verbose_name_plural = 'Строки заказа'