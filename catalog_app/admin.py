from django.contrib import admin
from django.utils.html import format_html
from catalog_app.models import Category, Good, Producer


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ("name", "id")
    search_fields = ["name"]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "comment",
                )
            },
        ),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "preview", "parent", "id")
    search_fields = ["name"]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    (
                        "name",
                        "parent",
                    ),
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
    list_display = ("name", "art", "code", "category", "producer", "preview", "id")
    search_fields = ["name", "art"]
    list_filter = ["not_active", "category", "producer"]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    ("name", "category"),
                    "producer",
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
