from django.contrib import admin

from django import forms

from .models import Good, Category, Property, Value, GoodsPropertyValue, Picture

class PictureInline(admin.TabularInline):
    model = Picture
    exclude = ('title', 'slug')
    extra = 0

class ValueInline(admin.TabularInline):
    model = Value
    exclude = ('slug',)
    extra = 0


class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
    )

    inlines = [ValueInline, ]

    list_filter = ('category',)

    exclude = ('slug',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    # inlines = [PictureInline, ]

    # list_filter = ('is_sale', 'is_new', 'is_hot')

    exclude = ('slug',)


class GoodAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'full_name',
        'category',
        'is_sale',
        'is_new',
        'is_hot'
    )

    inlines = [PictureInline, ]

    list_filter = ('is_sale', 'is_new', 'is_hot')

    exclude = ('slug',)


class GoodsPropertyValueAdmin(admin.ModelAdmin):
    list_display = (
        'good',
        'property',
        'value'
    )

    list_filter = ('good', 'property', 'value')


admin.site.register(Property, PropertyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(GoodsPropertyValue, GoodsPropertyValueAdmin)
admin.site.register(Good, GoodAdmin)
