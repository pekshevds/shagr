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
    )



class GoodAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'full_name',
        'is_sale',
        'is_new',
        'is_hot',
        'is_service'
    )

    inlines = [PictureInline, GoodsPropertyValueInline, ]

    list_filter = ('is_sale', 'is_new', 'is_hot', 'is_service', 'category')

    exclude = ('uid_1c',)



admin.site.register(Property, PropertyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Good, GoodAdmin)
admin.site.register(PropertySetTemplate)
admin.site.register(Offer)
