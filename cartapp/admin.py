from django.contrib import admin

# Register your models here.
from .models import Cart
# Register your models here.
class CartAdmin(admin.ModelAdmin):
	list_display = (
					'user',					
					)
	list_filter = ( 'user',)
	
admin.site.register(Cart, CartAdmin)
