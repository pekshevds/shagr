from django.shortcuts import render
from .main import get_hierarchy_categoryes, find_category_by_slug, find_good_by_slug, get_childs, get_goods
from .models import Category, Good

def show_catalog(request):

	return render_list(request, None)


def show_list(request, slug):

	
	return render_list(request, find_category_by_slug(slug))


def show_item(request, slug):

	good = find_good_by_slug(slug=slug)
	childs = get_childs(parent=good.category)

	context = {

		'categories': get_hierarchy_categoryes(),
		'parent'	: good.category,
		'childs'	: childs,
		'good'	    : good,

	}
	return render(request, 'catalogapp/item.html', context)


def render_list(request, parent):

	childs = get_childs(parent=parent)
	goods = get_goods(category=parent)
	

	context = {

		'categories': get_hierarchy_categoryes(),
		'parent'	: parent,
		'childs'	: childs,
		'goods'		: goods,

	}
	
	return render(request, 'catalogapp/list.html', context)
