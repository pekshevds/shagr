from django.shortcuts import render
from django.shortcuts import redirect

from .core import get_hierarchy_categoryes
from .core import find_category_by_slug
from .core import find_good_by_slug
from .core import get_childs
from .core import get_goods
from .core import get_brands_goods
from .core import get_brands
from .core import get_search
from .core import add_review



from wishlistapp.core import get_wishlist
from shagr.core import get_context

from django.core.paginator import Paginator


def search(request):
	
	search = request.GET.get('search', "")

	if search != "":#Это поиск по имени
		goods = get_search(name=search)
		search = "&search=" + search
	else:#Фильтры
		search = "&"
		brands = set()
		for brand in get_brands():
			if request.GET.get(brand.slug, "") == "on":
				brands.add(brand)
				search = search + brand.slug + "=on" + "&"
		if search != "":
			search = search.rstrip('&')

		goods = get_brands_goods(brands)		

	
	return render_list(request, goods, None, search)


def render_list(request, goods, parent, addon=""):

	goods_count = 15

	childs = get_childs(parent=parent)
		

	page_number = request.GET.get('page', 1)
	paginator = Paginator(goods, goods_count)
	page = paginator.get_page(page_number)
	is_paginated = page.has_other_pages()
	

	context = get_context(request, parent)
	
	context['parent'] = parent
	context['childs'] = childs
	context['goods_count'] = len(goods)
	context['page'] = page
	context['is_paginated'] = is_paginated
	context['addon'] = addon
	
	return render(request, 'catalogapp/list.html', context)


def show_catalog(request):


	return render_list(request, get_goods(), None)


def show_list(request, slug):
	
	parent = find_category_by_slug(slug)
	goods = get_goods(category=parent)
	return render_list(request, goods, parent)


def show_item(request, slug):
	
	
	good = find_good_by_slug(slug=slug)
	if not good:
		return redirect(request.META['HTTP_REFERER'])	

	context = get_context(request)

	parent = good.category
	childs = get_childs(parent=parent)
	

	context['parent'] = parent
	context['childs'] = childs
	context['good'] = good
	
	return render(request, 'catalogapp/item.html', context)


def new_review(request, slug):

	if request.user.is_authenticated:
		try:
			
			add_review(user=request.user,
				slug=slug,				
				review=request.POST.get("review", ""),
				rating=request.POST.get("rating", 5))
		except:			
			pass

	return redirect(request.META['HTTP_REFERER'])

