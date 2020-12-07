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
from .core import get_rating_of_good


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
	rating = get_rating_of_good(good=good)
	context = {

		'categories'			: get_hierarchy_categoryes(),
		'parent'				: good.category,
		'childs'				: childs,
		'good'	    			: good,
		'properties_and_values'	: properties_and_values,
		'pictures'				: pictures,
		'reviews'				: reviews,
		'rating'				: rating,
	}
	return render(request, 'catalogapp/item.html', context)


def new_review(request, slug):
	try:
		
		add_review(slug=slug, 
					author=request.POST["author"], 
					email=request.POST["email"], 
					review=request.POST["review"], 
					rating=request.POST["rating"])
	except:
		pass

	return redirect(show_item, slug=slug)

def add_to_card(request, slug):

	try:
		quant = request.POST['quant']
	except:
		quant = 1
	
	good = find_good_by_slug(slug=slug)
	if good:
		print(good, ' - ', str(quant))
		parent = good.category
	return request.META['HTTP_REFERER']