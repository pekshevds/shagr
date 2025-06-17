from typing import Any
from django.db import models
from django.db.models import QuerySet
from index_app.models import Directory

DEFAULT_EXTENTION = "jpg"


def fetch_image_name(
    prefix: str, instance: Any, extension: str = DEFAULT_EXTENTION
) -> str:
    return f"images/{prefix}_{str(instance.id)}.{extension}"


def fetch_extention_from_filename(filename: str) -> str:
    parts_of_filename = filename.split(".")
    if len(parts_of_filename) == 2:
        return parts_of_filename[1]
    return DEFAULT_EXTENTION


def get_image_name1(instance: object, filename: str) -> str:
    extention = fetch_extention_from_filename(filename)
    return fetch_image_name("image1", instance, extention)


def get_image_name2(instance: object, filename: str) -> str:
    extention = fetch_extention_from_filename(filename)
    return fetch_image_name("image2", instance, extention)


def get_image_name3(instance: object, filename: str) -> str:
    extention = fetch_extention_from_filename(filename)
    return fetch_image_name("image3", instance, extention)


def get_image_name4(instance: object, filename: str) -> str:
    extention = fetch_extention_from_filename(filename)
    return fetch_image_name("image4", instance, extention)


class Producer(Directory):
    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"


class Category(Directory):
    image1 = models.ImageField(
        verbose_name="Превью", upload_to=get_image_name1, blank=True, null=True
    )
    parent = models.ForeignKey(
        "Category",
        verbose_name="Родитель",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="children",
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
        verbose_name_plural = "Категории"


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
    image1 = models.ImageField(
        verbose_name="Изображение 1", upload_to=get_image_name1, blank=True, null=True
    )
    image2 = models.ImageField(
        verbose_name="Изображение 2", upload_to=get_image_name2, blank=True, null=True
    )
    image3 = models.ImageField(
        verbose_name="Изображение 3", upload_to=get_image_name3, blank=True, null=True
    )
    image4 = models.ImageField(
        verbose_name="Изображение 4", upload_to=get_image_name4, blank=True, null=True
    )
    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="goods",
    )
    producer = models.ForeignKey(
        Producer,
        verbose_name="Производитель",
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
    objects = models.Manager()
    active_items = ActiveGoodsManager()

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
