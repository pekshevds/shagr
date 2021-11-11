from django.shortcuts import render, redirect

from catalogapp.core import find_good_by_slug

from .core import get_wishlist
from .core import add_to_wishlist
from .core import del_from_wishlist
from .core import clear_wishlist

from shagr.core import get_context

# Create your views here.
def show_wishlist(request):
	# if request.user.is_authenticated:	
	return render(request, 'wishlistapp/wishlist.html', get_context(request))
	# return redirect(request.META['HTTP_REFERER'])


def add_good_to_wishlist(request, slug):
	
	if request.user.is_authenticated:
		good = find_good_by_slug(slug=slug)
		if good:
		
			wishlist = get_wishlist(request)
			add_to_wishlist(wishlist, good)		

	return redirect(request.META['HTTP_REFERER'])

def del_good_from_wishlist(request, slug):
	
	if request.user.is_authenticated:
		good = find_good_by_slug(slug=slug)
		if good:

			wishlist = get_wishlist(request)
			del_from_wishlist(wishlist, good)		

	return redirect(request.META['HTTP_REFERER'])

def clear_current_wishlist(request):
	
	if request.user.is_authenticated:
		wishlist = get_wishlist(request)
		clear_wishlist(wishlist)		

	return redirect(request.META['HTTP_REFERER'])