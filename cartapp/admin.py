from django.contrib import admin
from .models import Cart
from .models import CartItem
# Register your models here.

class CartItemline(admin.TabularInline):
    model = CartItem    
    extra = 0

class CartAdmin(admin.ModelAdmin):
	list_display = (
					'user',					
					)
	list_filter = ( 'user',)
	inlines = [CartItemline,]
	
admin.site.register(Cart, CartAdmin)
