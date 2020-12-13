from django.shortcuts import render
from django.shortcuts import redirect

from shagr.core import get_context


from .core import get_orders
from .core import get_order
from .core import del_from_order
from .core import add_to_order

# Create your views here.

def show_orders(request):

	context = get_context(request)
	if request.user.is_authenticated:
		context['orders'] = get_orders(context['buyer'])
	return render(request, 'orderapp/orders.html', context)


def show_order(request, id):

	context = get_context(request)
	
	if request.user.is_authenticated:
		context['order'] = get_order(id)
	return render(request, 'orderapp/order.html', context)


def del_good_from_order(request, id):
	
	if request.user.is_authenticated:
		del_from_order(id)
	return redirect(request.META['HTTP_REFERER'])

def add_good_to_order(request, slug):
	
	if request.user.is_authenticated:
		add_to_order(request, slug)

	return redirect(request.META['HTTP_REFERER'])

