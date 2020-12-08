from django.contrib import admin
from .models import WishList
# Register your models here.
class WishListAdmin(admin.ModelAdmin):
	list_display = (
					'user',					
					)
	list_filter = ( 'user',)
	
admin.site.register(WishList, WishListAdmin)

