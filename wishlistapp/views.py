from django.shortcuts import render, redirect

from catalogapp.core import get_hierarchy_categoryes
from catalogapp.core import get_childs
from catalogapp.core import get_goods_with_main_properties_and_values
from catalogapp.core import find_good_by_slug

from cartapp.core import get_cart

from .core import get_wishlist
from .core import add_to_wishlist
from .core import del_from_wishlist



# Create your views here.
def show_wishlist(request):
	
	wishlist = get_wishlist(request)	

	# goods = get_goods_with_main_properties_and_values(wishlist['goods'])
	childs = get_childs(parent=None)

	cart = get_cart(request)
	wishlist = get_wishlist(request)

	context = {
	'categories'			: get_hierarchy_categoryes(),
	'parent'				: None,
	'childs'				: childs,	
	'wishlist'				: wishlist['items'],
	'wishlist_count'		: wishlist['wishlist_count'],
	'cart_quant'			: cart['cart_quant'],
	'cart_sum'				: cart['cart_sum'],
	
	}
	return render(request, 'wishlistapp/wishlist.html', context)


def add_good_to_wishlist(request, slug):
	
	good = find_good_by_slug(slug=slug)
	if good:
		
		wishlist = get_wishlist(request)
		add_to_wishlist(wishlist, good)		

	return redirect(request.META['HTTP_REFERER'])

def del_good_from_wishlist(request, slug):
	
	good = find_good_by_slug(slug=slug)
	if good:

		wishlist = get_wishlist(request)
		del_from_wishlist(wishlist, good)		

	return redirect(request.META['HTTP_REFERER'])