from django.contrib import admin
from .models import WishList
from .models import WishListItem
# Register your models here.

class WishListItemline(admin.TabularInline):
    model = WishListItem    
    extra = 0

class WishListAdmin(admin.ModelAdmin):
	list_display = (
					'user',					
					)
	list_filter = ( 'user',)
	inlines = [WishListItemline,]

	
admin.site.register(WishList, WishListAdmin)

