from django.test import TestCase

# Create your tests here.
import json
import os
from .models import Good, Category, Brand


def download_goods_from_json(data):
    for i in data['goods']:
    	# print(i['name'])
        good = Good()
        good.name = i['name']
        good.uid_1c = i['uid_1c']
        good.code_1c = i['code_1c']
        good.art = i['art']
        good.category_uid_1с = i['category_uid_1с']
        good.description = i['description']
       	good.is_service = i['is_service'] == "True"
        good.save()

def download_goods_from_file():
    path = os.path.abspath('catalogapp/goods.json')

    with open(path, 'r', encoding="utf-8-sig") as f:

        # print(f.read())

        data = json.loads(f.read())
        download_goods_from_json(data)
    f.close()

def delete_all_goods():
	Good.objects.all().delete()

def parse_goods():
	for good in Good.objects.all():

		queryset = Category.objects.filter(uid_1c=good.category_uid_1с)
		if queryset:
			good.category = queryset[0]
			good.save()


def download_categoryes_from_json(data):
    for i in data['goods']:
    	# print(i['name'])
        ctegory = Category()
        ctegory.name = i['name']
        ctegory.uid_1c = i['uid_1c']
        ctegory.parent_uid_1c = i['parent_uid_1c']
        ctegory.save()

def download_categoryes_from_file():
    path = os.path.abspath('catalogapp/groups.json')

    with open(path, 'r', encoding="utf-8-sig") as f:

        # print(f.read())

        data = json.loads(f.read())
        download_categoryes_from_json(data)
    f.close()

def parse_categoryes():
	for category in Category.objects.all():

		queryset = Category.objects.filter(uid_1c=category.parent_uid_1c)
		if queryset:
			category.parent = queryset[0]
			category.save()

def delete_all_categoryes():

    for category in Category.objects.all():
        category.parent = None
        category.save()

    Category.objects.all().delete()

def make_all():
	download_categoryes_from_file()
	parse_categoryes()
	download_goods_from_file()
	parse_goods()


def set_brand_by_name(name=''):

    brand = Brand.objects.filter(name__icontains=name).first()

    for good in Good.objects.filter(name__icontains=name):
        
        good.brand = brand
        good.save()

    # from catalogapp.tests import set_brand_by_name
    # set_brand_by_name(name='bosch')
    # 

def set_brands_by_name():

    for brand in Brand.objects.all():
        print(brand.name)
        for good in Good.objects.filter(name__icontains=brand.name):
            print("    " + good.name)
            good.brand = brand
            good.save()

    # from catalogapp.tests import set_brands_by_name
    # set_brand_by_name(name='bosch')
    #


def cleare_brands():    
    for good in Good.objects.all():            
            good.brand = None
            good.save()

    
def set_show():
    for good in Good.objects.filter(quant__gt=0):
        
        good.is_show = True
        good.save()
    # from catalogapp.tests import set_show
    # set_show()