from django.shortcuts import render, redirect

from catalogapp.core import find_good_by_slug

from .core import get_wishlist
from .core import add_to_wishlist
from .core import del_from_wishlist

from shagr.core import get_context

# Create your views here.
def show_wishlist(request):
		
	return render(request, 'wishlistapp/wishlist.html', get_context(request))


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