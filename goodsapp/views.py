from django.shortcuts import render
from baseapp.views import get_all_categories
from goodsapp.models import Category

def show_catalog(request):

	context = {

		'categories' : get_all_categories(),

	}
	
	return render(request, 'goodsapp/catalog.html', context)


def show_category(request, slug):

	try:
		parent = Category.objects.get(slug=slug)
		childs = Category.objects.filter(parent=parent)
	except Category.DoesNotExist:
		childs = Category.objects.all()
	

	context = {

		'categories' : get_all_categories(),
		'childs'	: childs,
		'parent'	: parent,

	}
	
	return render(request, 'goodsapp/category.html', context)
