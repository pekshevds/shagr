from django.shortcuts import render, redirect
from catalogapp.core import get_hierarchy_categoryes
from catalogapp.core import get_childs
from .core import get_wishlist
from .core import add_to_wishlist
from .core import del_from_wishlist
from .core import get_count_wishlist

from catalogapp.core import get_goods_with_main_properties_and_values
from catalogapp.core import find_good_by_slug

# Create your views here.
def show_wishlist(request):
	
	wishlist = get_wishlist(request)	

	goods = get_goods_with_main_properties_and_values(wishlist['goods'])
	childs = get_childs(parent=None)

	context = {
	'categories'			: get_hierarchy_categoryes(),
	'parent'				: None,
	'childs'				: childs,	
	'wishlist'				: goods,
	'wishlist_count'		: get_count_wishlist(request),
	}
	return render(request, 'wishlistapp/wishlist.html', context)


def add_good_to_wishlist(request, slug):
	
	good = find_good_by_slug(slug=slug)
	if good:
		add_to_wishlist(request, good)		

	return redirect(request.META['HTTP_REFERER'])

def del_good_from_wishlist(request, slug):
	
	good = find_good_by_slug(slug=slug)
	if good:
		del_from_wishlist(request, good)		

	return redirect(request.META['HTTP_REFERER'])