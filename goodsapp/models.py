from django.db import models
# from smart_selects.db_fields import ChainedForeignKey
import uuid


def get_uuid():
    # return str(uuid.uuid4().fields[0])
    return str(uuid.uuid4())

def get_image_name(instance, filename):
    new_name = ('%s' + '.' + filename.split('.')[-1]) % instance.slug
    return new_name


# Create your models here.

class Value(models.Model):
    slug = models.SlugField(max_length=36, verbose_name='Url', blank=True, db_index=True)
    name = models.CharField(max_length=255, verbose_name="Наименование", null=True)

    property = models.ForeignKey(
        'Property',
        on_delete=models.CASCADE, verbose_name="Свойство", null=False
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug == "":
            self.slug = get_uuid()

        super(Value, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Значение'
        verbose_name_plural = 'Значения'


class Property(models.Model):
    slug = models.SlugField(max_length=36, verbose_name='Url', blank=True, db_index=True)
    name = models.CharField(max_length=255, verbose_name="Наименование", null=True)

    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE, verbose_name="Категория", null=False
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug == "":
            self.slug = get_uuid()

        super(Property, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Свойство'
        verbose_name_plural = 'Свойства'


class Category(models.Model):
    slug = models.SlugField(max_length=36, verbose_name='Url', blank=True, db_index=True)
    name = models.CharField(max_length=255, verbose_name="Наименование", null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug == "":
            self.slug = get_uuid()

        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class ObjectPropertyValue(models.Model):
    good = models.ForeignKey(
        'Good',
        on_delete=models.CASCADE, verbose_name="Номенклатура", null=False
    )

    property = models.ForeignKey(
        'Property',
        on_delete=models.CASCADE, verbose_name="Свойство", null=False
    )

    value = models.ForeignKey(
        'Value',
        on_delete=models.CASCADE, verbose_name="Значение", null=False
    )

    # value = ChainedForeignKey(
    #     'Value',
    #     on_delete=models.CASCADE,
    #     verbose_name="Значение",
    #     null=False,
    #     chained_field="property",
    #     chained_model_field="property",
    #     show_all=False,
    #     auto_choose=True
    # )

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):

        super(ObjectPropertyValue, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Значение свойства'
        verbose_name_plural = 'Значения свойств'


class Good(models.Model):
    slug = models.SlugField(max_length=36, verbose_name='Url', blank=True, db_index=True)
    name = models.CharField(max_length=255, verbose_name="Наименование", null=True)
    art = models.CharField(max_length=25, verbose_name="Артикул", null=True, blank=True)
    full_name = models.TextField(verbose_name="Наименование полное", null=True, blank=True)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)

    is_sale = models.BooleanField(verbose_name="Распродажа")
    is_new = models.BooleanField(verbose_name="Новинка")
    is_hot = models.BooleanField(verbose_name="Спецпредложение")

    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT, verbose_name="Категория", null=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug == "":
            self.slug = get_uuid()

        super(Good, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Номенклатура'
        verbose_name_plural = 'Номенклатура'
