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
		'comment',
	)
	
	inlines = [OrderItemInline,]
	search_fields = ('id',)

admin.site.register(Order, OrderAdmin)