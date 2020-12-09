from django.shortcuts import render, redirect

from wishlistapp.core import get_count_wishlist

from catalogapp.core import get_hierarchy_categoryes
from catalogapp.core import get_childs
from catalogapp.core import find_good_by_slug

from .core import get_cart
from .core import add_to_cart
from .core import del_from_cart
from .core import get_count_cart
from .core import get_sum_cart



# Create your views here.
def show_cart(request):
	
	cart = get_cart(request)	

	childs = get_childs(parent=None)

	context = {
	'categories'			: get_hierarchy_categoryes(),
	'parent'				: None,
	'childs'				: childs,	
	'cart'					: cart['items'],
	'cart_count'			: get_count_cart(request),
	'wishlist_count'		: get_count_wishlist(request),
	'cart_sum'				: get_sum_cart(request),
	}
	return render(request, 'cartapp/cart.html', context)


def add_good_to_cart(request, slug):
	good = find_good_by_slug(slug=slug)
	quant = request.POST.get('quant', 1)
	if good:
		add_to_cart(request, good, quant=quant)		

	return redirect(request.META['HTTP_REFERER'])
	

def del_good_from_cart(request, slug):
	
	good = find_good_by_slug(slug=slug)
	if good:
		del_from_cart(request, good)		

	return redirect(request.META['HTTP_REFERER'])