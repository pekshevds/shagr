from django.db import models
from django.db.models import QuerySet
from index_app.models import Directory


class Category(Directory):
    image = models.ImageField(
        verbose_name="Превью", upload_to="images/", blank=True, null=True
    )
    seo_title = models.TextField(
        verbose_name="<title>", null=True, blank=True, default=""
    )
    seo_description = models.TextField(
        verbose_name="<description>",
        null=True,
        blank=True,
        default="",
    )
    seo_keywords = models.TextField(
        verbose_name="<keywords>",
        null=True,
        blank=True,
        default="",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Котегории"


class ActiveGoodsManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(not_active=False)


class Good(Directory):
    art = models.CharField(
        verbose_name="Артикул",
        max_length=50,
        blank=True,
        null=True,
        db_index=True,
        default="",
    )
    code = models.CharField(
        verbose_name="Код (для 1С)",
        max_length=11,
        blank=True,
        null=True,
        db_index=True,
        default="",
    )
    full_name = models.TextField(
        verbose_name="Наименование полное", blank=True, null=True
    )
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    image = models.ImageField(
        verbose_name="Превью", upload_to="images/", blank=True, null=True
    )
    image1 = models.ImageField(
        verbose_name="Изображение 1", upload_to="images/", blank=True, null=True
    )
    image2 = models.ImageField(
        verbose_name="Изображение 2", upload_to="images/", blank=True, null=True
    )
    image3 = models.ImageField(
        verbose_name="Изображение 3", upload_to="images/", blank=True, null=True
    )
    image4 = models.ImageField(
        verbose_name="Изображение 4", upload_to="images/", blank=True, null=True
    )
    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="goods",
    )
    not_active = models.BooleanField(verbose_name="Не активный", default=False)
    seo_title = models.TextField(
        verbose_name="<title>", null=True, blank=True, default=""
    )
    seo_description = models.TextField(
        verbose_name="<description>",
        null=True,
        blank=True,
        default="",
    )
    seo_keywords = models.TextField(
        verbose_name="<keywords>",
        null=True,
        blank=True,
        default="",
    )
    active_items = ActiveGoodsManager()

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
