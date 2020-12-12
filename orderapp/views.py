from django.shortcuts import render
from django.shortcuts import redirect

from shagr.core import get_context
from .core import get_orders
from .core import get_order

# Create your views here.

def show_orders(request):

	context = get_context(request)
	context['orders'] = get_orders(context['buyer'])
	return render(request, 'orderapp/orders.html', context)


def show_order(request, id):

	context = get_context(request)
	context['order'] = get_order(id)

	return render(request, 'orderapp/order.html', context)