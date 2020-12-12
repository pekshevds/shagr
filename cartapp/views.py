from django.shortcuts import render, redirect

from catalogapp.core import find_good_by_slug

from .core import get_cart
from .core import add_to_cart
from .core import del_from_cart

from shagr.core import get_context

# Create your views here.
def show_cart(request):
		
	return render(request, 'cartapp/cart.html', get_context(request))


def add_good_to_cart(request, slug):
	good = find_good_by_slug(slug=slug)
	quant = request.POST.get('quant', 1)
	if good:

		cart = get_cart(request)
		add_to_cart(cart, good, quant=quant)		

	return redirect(request.META['HTTP_REFERER'])
	

def del_good_from_cart(request, slug):
	
	good = find_good_by_slug(slug=slug)
	if good:

		cart = get_cart(request)
		del_from_cart(cart, good)		

	return redirect(request.META['HTTP_REFERER'])