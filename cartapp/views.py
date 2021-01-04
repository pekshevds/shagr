from decimal import Decimal

from django.shortcuts import render
from django.shortcuts import redirect

from catalogapp.core import find_good_by_slug

from .core import get_cart
from .core import add_to_cart
from .core import insert_to_cart
from .core import del_from_cart
from .core import clear_cart

from shagr.core import get_context

# Create your views here.
def show_cart(request):
	context = get_context(request)
	# print(context['cart'].get_items()[0].get_amount())
	return render(request, 'cartapp/cart.html', context)


def add_good_to_cart(request, slug):
	
	good = find_good_by_slug(slug=slug)
	quant = int(request.POST.get('quant', 1))	
	if good:

		cart = get_cart(request)
		add_to_cart(cart, good, quant=quant)	

	return redirect(request.META['HTTP_REFERER'])


def insert_good_to_cart(request, slug):

	good = find_good_by_slug(slug=slug)
	quant = int(request.POST.get('quant', 1))
	if good:

		cart = get_cart(request)
		insert_to_cart(cart, good, quant=quant)		

	return redirect(request.META['HTTP_REFERER'])
	

def del_good_from_cart(request, slug):
	
	good = find_good_by_slug(slug=slug)
	if good:

		cart = get_cart(request)
		del_from_cart(cart, good)		

	return redirect(request.META['HTTP_REFERER'])

def clear_current_cart(request):
	
	cart = get_cart(request)
	clear_cart(cart)		

	return redirect(request.META['HTTP_REFERER'])