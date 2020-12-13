from django.contrib import admin
from .models import Order
from .models import OrderItem

# Register your models here.


class OrderItemInline(admin.TabularInline):
	model = OrderItem
	extra = 0

class OrderAdmin(admin.ModelAdmin):
	list_display = (		
		'id',
		'date',
		'buyer',
		'total',
		'payment_status',
		'delivery_status',
		'comment',
	)
	
	inlines = [OrderItemInline,]
	search_fields = ('id',)
	list_filter = ( 'payment_status', 'delivery_status',)
	
	

admin.site.register(Order, OrderAdmin)