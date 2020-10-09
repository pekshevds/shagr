from django.db import models
# from smart_selects.db_fields import ChainedForeignKey
import uuid

from django.template.defaultfilters import slugify
from unidecode import unidecode


def get_uuid4():
    return str(uuid.uuid4())


def get_uuid():
    return str(uuid.uuid4().fields[0])


def get_image_name(instance, filename):
    new_name = ('%s' + '.' + filename.split('.')[-1]) % instance.slug
    return new_name


# Create your models here.

class Value(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование", null=True)

    property = models.ForeignKey(
        'Property',
        on_delete=models.CASCADE, verbose_name="Свойство", null=False
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Value, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Значение'
        verbose_name_plural = 'Значения'


class PropertySetTemplate(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование", null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(PropertySetTemplate, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Шаблон наборов свойств'
        verbose_name_plural = 'Шаблоны наборов свойств'


class Property(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование", null=True)
    template = models.ManyToManyField(PropertySetTemplate, verbose_name="Шаблон", blank=True)

    slug = models.SlugField(max_length=300, verbose_name='Url', blank=True, db_index=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))

        super(Property, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Свойство'
        verbose_name_plural = 'Свойства'


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование", null=True)
    parent = models.ForeignKey('Category', verbose_name="Родитель", on_delete=models.PROTECT, blank=True, null=True)
    picture = models.ImageField(upload_to=get_image_name, verbose_name='Изображение 200х200', default=None, null=True, blank=True)
    slug = models.SlugField(max_length=300, verbose_name='Url', blank=True, db_index=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))

        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class GoodsPropertyValue(models.Model):
    good = models.ForeignKey('Good', verbose_name="Номенклатура", on_delete=models.CASCADE, null=False)
    property = models.ForeignKey('Property', verbose_name="Свойство", on_delete=models.CASCADE, null=False)
    value = models.ForeignKey('Value', verbose_name="Значение", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.property) + ': ' + str(self.value)

    class Meta:
        verbose_name = 'Значение свойства'
        verbose_name_plural = 'Значения свойств'


class Good(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование", null=True)
    site_name = models.CharField(max_length=255, verbose_name="Наименование для магазина", null=True, blank=True)
    art = models.CharField(max_length=25, verbose_name="Артикул", null=True, blank=True)    
    full_name = models.TextField(verbose_name="Наименование для магазина (не использовать)", null=True, blank=True)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    slug = models.SlugField(max_length=300, verbose_name='Url', blank=True, db_index=True)

    is_sale = models.BooleanField(verbose_name="Распродажа", default=False)
    is_new = models.BooleanField(verbose_name="Новинка", default=False)
    is_hot = models.BooleanField(verbose_name="Спецпредложение", default=False)
    is_service = models.BooleanField(verbose_name="Услуга", default=False)
    is_show = models.BooleanField(verbose_name="Виден для пользователей", default=False)
    uid_1c = models.SlugField(max_length=36, verbose_name='Идентификатор в 1С', null=True, blank=True)
    code_1c = models.CharField(max_length=11, verbose_name="Код 1С", null=True, blank=True)

    template = models.ForeignKey('PropertySetTemplate', verbose_name="Шаблон набора свойств", on_delete=models.PROTECT, blank=True, null=True)
    brand = models.ForeignKey('Brand', verbose_name="Бренд", on_delete=models.PROTECT, blank=True, null=True)
    category = models.ForeignKey('Category', verbose_name="Категория", on_delete=models.PROTECT, blank=True, null=True)
    

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.uid_1c == "":
            self.uid_1c = get_uuid4()

        self.slug = slugify(unidecode(self.site_name))

        super(Good, self).save(*args, **kwargs)

        queryset = GoodsPropertyValue.objects.filter(good=self)
        if not self.template is None and len(queryset) == 0:

            properties = Property.objects.filter(template=self.template)
            for property in properties:
                
                record = GoodsPropertyValue()
                record.good = self
                record.property = property
                try:
                    record.save()
                except:
                    continue
               

    class Meta:
        verbose_name = 'Номенклатура'
        verbose_name_plural = 'Номенклатура'


class Picture(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование', blank=True)
    slug = models.SlugField(max_length=36, verbose_name='Url', blank=True, db_index=True)
    good = models.ForeignKey('Good', verbose_name='Номенклатура', on_delete=models.CASCADE)
    images = models.ImageField(upload_to=get_image_name, verbose_name='Изображение 370x220', default=None, null=True, blank=True)
    main_image = models.BooleanField(verbose_name='Основная картинка', default=False)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        if self.slug == "":
            self.slug = get_uuid()
            self.title = self.slug

        super(Picture, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

class Brand(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование", null=True)    
    picture = models.ImageField(upload_to=get_image_name, verbose_name='Изображение 200х200', default=None, null=True, blank=True)
    slug = models.SlugField(max_length=300, verbose_name='Url', blank=True, db_index=True)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))

        super(Brand, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

class Offer(models.Model):
    good = models.ForeignKey('Good', verbose_name="Номенклатура", on_delete=models.PROTECT, blank=True, null=True)

    price = models.DecimalField(verbose_name='Цена', default=0, max_digits=15, decimal_places=2)
    quant = models.DecimalField(verbose_name='Количество', default=0, max_digits=15, decimal_places=3)
    date = models.DateTimeField(verbose_name='Период', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'
