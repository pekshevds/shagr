from django.contrib import admin
from .models import Buyer

class BuyerAdmin(admin.ModelAdmin):
	list_display = (
					'user', 
					'first_name',
					'last_name',
					'phone',
					'address',
					)

admin.site.register(Buyer, BuyerAdmin)

