from django.shortcuts import render
from django.shortcuts import redirect

from .core import get_hierarchy_categoryes
from .core import find_category_by_slug
from .core import find_good_by_slug
from .core import get_childs
from .core import get_goods
from .core import get_properties_and_values
from .core import get_goods_with_main_properties_and_values
from .core import get_good_pictures
from .core import add_review
from .core import get_good_reviews


from django.core.paginator import Paginator

def render_list(request, parent):

	goods_count = 15

	childs = get_childs(parent=parent)
	goods = get_goods_with_main_properties_and_values(category=parent)
	

	page_number = request.GET.get('page', 1)
	paginator = Paginator(goods, goods_count)
	page = paginator.get_page(page_number)
	is_paginated = page.has_other_pages()
	


	context = {

		'categories'			: get_hierarchy_categoryes(),
		'parent'				: parent,
		'childs'				: childs,
		'goods_count'			: len(goods),
		'page'					: page,
		'is_paginated'			: is_paginated,	

	}	
	return render(request, 'catalogapp/list.html', context)


def show_catalog(request):

	return render_list(request, None)


def show_list(request, slug):
	
	return render_list(request, find_category_by_slug(slug))


def show_item(request, slug):

	good = find_good_by_slug(slug=slug)
	childs = get_childs(parent=good.category)
	properties_and_values = get_properties_and_values(good=good)
	pictures = get_good_pictures(good=good)
	reviews = get_good_reviews(good=good)

	context = {

		'categories'			: get_hierarchy_categoryes(),
		'parent'				: good.category,
		'childs'				: childs,
		'good'	    			: good,
		'properties_and_values'	: properties_and_values,
		'pictures'				: pictures,
		'reviews'				: reviews,		
	}
	return render(request, 'catalogapp/item.html', context)


def new_review(request, slug):
	_author = request.POST["author"]
	_email = request.POST["email"]
	_review = request.POST["review"]
	_rating = request.POST["rating"]	

	add_review(slug=slug, author=_author, email=_email, review=_review, rating=_rating)
	return redirect(show_item, slug=slug)