from django.contrib import admin

from django import forms

from .models import Good
from .models import Category
from .models import Property
from .models import Value
from .models import GoodsPropertyValue
from .models import Picture
from .models import PropertySetTemplate
from .models import Offer
from .models import Brand


class PictureInline(admin.TabularInline):
    model = Picture
    exclude = ('title', 'slug')
    extra = 0


class GoodsPropertyValueInlineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GoodsPropertyValueInlineForm, self).__init__(*args, **kwargs)
        try:
            self.fields['value'].queryset = Value.objects.filter(property=self.instance.property)
        except:
            self.fields['value'].queryset = Value.objects


class GoodsPropertyValueInline(admin.TabularInline):
    model = GoodsPropertyValue
    form = GoodsPropertyValueInlineForm
    extra = 0


class ValueInline(admin.TabularInline):
    model = Value
    extra = 0


class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    inlines = [ValueInline, ]



class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'parent',
        'grand_parent',
    )

    search_fields = ('name',)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        if db_field.name == "parent":
            kwargs["queryset"] = Category.objects.all().order_by('name')
            return super(CategoryAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def grand_parent(self, obj):

        grand_parent = None

        parent = obj.parent

        if parent:

            grand_parent = parent.parent

        return grand_parent


class GoodAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'full_name',
        'category',
        'brand',
        'is_sale',
        'is_new',
        'is_hot',
        'is_service',
        'is_show',        
    )

    inlines = [PictureInline, GoodsPropertyValueInline, ]

    list_filter = ( 'category', 'brand', 'is_sale', 'is_new', 'is_hot', 'is_service', 'is_show',)

    search_fields = ('name',)

    readonly_fields = ('code_1c',)

    exclude = ('uid_1c',)



class OfferAdmin(admin.ModelAdmin):
    list_display = (
        'good',
        'price',
        'quant',
    )

    readonly_fields = ('good',)

class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'name',        
    )


admin.site.register(Property, PropertyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Good, GoodAdmin)
admin.site.register(PropertySetTemplate)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Brand, BrandAdmin)
