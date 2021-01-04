from django.db import models
from django.contrib.auth.models import User

from django.template.defaultfilters import slugify
from unidecode import unidecode

from django.db.models import Avg, Max, Min, Sum

import uuid

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
        
        try:
            self.slug = slugify(unidecode(self.name))  
        except:
            pass
        

        super(Property, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Свойство'
        verbose_name_plural = 'Свойства'


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование", null=True)
    parent = models.ForeignKey('Category', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    picture = models.ImageField(upload_to=get_image_name, verbose_name='Изображение 200х200', default=None, null=True, blank=True)
    slug = models.SlugField(max_length=300, verbose_name='Url', blank=True, db_index=True)

    uid_1c = models.SlugField(max_length=36, verbose_name='Идентификатор в 1С', null=True, blank=True)
    parent_uid_1c = models.SlugField(max_length=36, verbose_name='Идентификатор родителя в 1С', null=True, blank=True)

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        
        try:
            self.slug = slugify(unidecode(self.name))  
        except:
            pass

        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class GoodsPropertyValue(models.Model):
    good = models.ForeignKey('Good', verbose_name="Номенклатура", on_delete=models.CASCADE, null=False)
    property = models.ForeignKey('Property', verbose_name="Свойство", on_delete=models.CASCADE, null=False)
    value = models.ForeignKey('Value', verbose_name="Значение", on_delete=models.CASCADE, null=True, blank=True)
    is_main = models.BooleanField(verbose_name="Основное", default=True)

    def __str__(self):
        return str(self.property) + ': ' + str(self.value)

    class Meta:
        verbose_name = 'Значение свойства'
        verbose_name_plural = 'Значения свойств'


class Good(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование", null=True)
    site_name = models.CharField(max_length=255, verbose_name="Наименование для магазина", null=True, blank=True)
    art = models.CharField(max_length=25, verbose_name="Артикул", null=True, blank=True, default='')    
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
    country = models.ForeignKey('Country', verbose_name="Страна", on_delete=models.PROTECT, blank=True, null=True)
    category = models.ForeignKey('Category', verbose_name="Категория", on_delete=models.PROTECT, blank=True, null=True)
    
    category_uid_1с = models.SlugField(max_length=36, verbose_name='Идентификатор категории в 1С', null=True, blank=True)

    price = models.DecimalField(verbose_name='Цена', default=0, max_digits=15, decimal_places=2)
    quant = models.PositiveIntegerField(verbose_name='Количество', default=0)

    width = models.DecimalField(verbose_name='Ширина, см', default=0, max_digits=15, decimal_places=1)
    height = models.DecimalField(verbose_name='Высота, см', default=0, max_digits=15, decimal_places=1)
    depth = models.DecimalField(verbose_name='Глубина, см', default=0, max_digits=15, decimal_places=1)
    weight = models.DecimalField(verbose_name='Вес, кг', default=0, max_digits=15, decimal_places=3)
    volume = models.DecimalField(verbose_name='Объем, м3', default=0, max_digits=15, decimal_places=5)

    def __str__(self):
        return self.name


    def get_reviews(self):
        try:
            reviews = Review.objects.filter(good=self).order_by('review_date')
        except:
            return None
        return reviews


    def get_reviews_count(self):
        
        reviews_count = 0
        
        reviews = self.get_reviews()
        if reviews:
            reviews_count = len(reviews)
            
        return reviews_count


    def get_rating(self):
        
        rating = 0


        reviews = self.get_reviews()
        if reviews:            

            reviews_count = len(reviews)
            rating_sum = reviews.aggregate(Sum('rating'))['rating__sum']
            rating = round(rating_sum / reviews_count)

        return rating


    def get_properties_and_values(self):
        try:
            records = GoodsPropertyValue.objects.filter(good=self)
        except:
            return None

        return records


    def get_main_properties_and_values(self):
        try:
            records = GoodsPropertyValue.objects.filter(good=self, is_main=True)[:5]
        except:
            return None

        return records


    def get_pictures(self):
        try:
            records = Picture.objects.filter(good=self)
        except:
            return None
        
        return records


    def get_main_picture(self):
        try:
            records = Picture.objects.filter(good=self, is_main=True)[:1]
        except:
            return None 

        if records:   
            return records[0]

        return None


    def save(self, *args, **kwargs):


        if not self.site_name:
            self.site_name = self.name

        if not self.uid_1c:
            self.uid_1c = get_uuid4()

        try:
            self.slug = slugify(unidecode(self.site_name))  
        except:
            pass

        volume = self.width/10 * self.height/10 * self.depth/10
        if self.volume == 0:
            self.volume = volume

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
    image = models.ImageField(upload_to=get_image_name, verbose_name='Изображение 500x500', default=None, null=True, blank=True)
    is_main = models.BooleanField(verbose_name='Основная картинка', default=False)

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
        
        try:
            self.slug = slugify(unidecode(self.site_name))  
        except:
            pass

        super(Brand, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Country(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование", null=True)    
    slug = models.SlugField(max_length=300, verbose_name='Url', blank=True, db_index=True)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        
        try:
            self.slug = slugify(unidecode(self.site_name))  
        except:
            pass

        super(Country, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Review(models.Model):    

    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.PROTECT, blank=False, null=False)
    good = models.ForeignKey('Good', verbose_name="Номенклатура", on_delete=models.PROTECT, blank=False, null=False)

    review = models.TextField(verbose_name="Отзыв")
    rating = models.PositiveSmallIntegerField(verbose_name="Оценка 1-5", default=5)
    review_date = models.DateTimeField(verbose_name="Дата отзыва", auto_now_add=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.email

    def save(self, *args, **kwargs):        
        super(Review, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
