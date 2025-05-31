from django.contrib import admin
from django.utils.html import format_html
from catalog_app.models import Category, Good


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "preview", "id")
    search_fields = ["name"]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "comment",
                    ("image", "preview"),
                )
            },
        ),
        (
            "CEO",
            {
                "fields": (
                    (
                        "seo_title",
                        "seo_description",
                        "seo_keywords",
                    )
                )
            },
        ),
    )
    readonly_fields = ("preview",)

    def preview(self, obj: Good) -> str:
        if obj.image:
            return format_html("'<img src={} style='max-height: 75px;'>", obj.image.url)
        return ""

    preview.short_description = "Изображение (превью)"


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ("name", "art", "code", "category", "preview", "id")
    search_fields = ["name", "art"]
    list_filter = ["not_active", "category"]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    ("name", "category"),
                    "full_name",
                    ("art", "code"),
                    "description",
                    "not_active",
                    "comment",
                )
            },
        ),
        (
            "Изображения",
            {
                "fields": (
                    ("image", "preview"),
                    ("image1", "image2"),
                    ("image3", "image4"),
                )
            },
        ),
        (
            "CEO",
            {
                "fields": (
                    (
                        "seo_title",
                        "seo_description",
                        "seo_keywords",
                    )
                )
            },
        ),
    )
    readonly_fields = ("preview",)

    def preview(self, obj: Good) -> str:
        if obj.image:
            return format_html("'<img src={} style='max-height: 75px;'>", obj.image.url)
        return ""

    preview.short_description = "Изображение (превью)"
