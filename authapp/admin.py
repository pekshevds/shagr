from django.contrib import admin
from .models import Buyer

class BuyerAdmin(admin.ModelAdmin):
	list_display = (			
					'last_name',		 
					'first_name',
					'middle_name',					
					'phone',
					'address',
					'user',
					)
	
search_fields = ('last_name',)

admin.site.register(Buyer, BuyerAdmin)

