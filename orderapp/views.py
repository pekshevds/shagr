from django.shortcuts import render
from django.shortcuts import redirect

from shagr.core import get_context


from .core import get_orders
from .core import get_order
from .core import del_from_order
from .core import add_to_order
from .core import create_order_from_cart
from .core import change_payment_status_of_order
from .core import send_mail_with_order


def show_orders(request):

	context = get_context(request)
	if request.user.is_authenticated:
		context['orders'] = get_orders(context['buyer'])
	return render(request, 'orderapp/orders.html', context)


def send_cart_to_order(request):

	order = create_order_from_cart(request)	
	if order:
		
		send_mail_with_order(request, order)

		return redirect('show_order', id=order.id)

	return redirect(request.META['HTTP_REFERER'])


def show_order(request, id):

	context = get_context(request)
		
	context['order'] = get_order(id)
	return render(request, 'orderapp/order.html', context)


def pay_for_order(request, id):

	change_payment_status_of_order(id)
	return redirect(request.META['HTTP_REFERER'])


def del_good_from_order(request, id):
	
	del_from_order(id)
	return redirect(request.META['HTTP_REFERER'])


def add_good_to_order(request, slug):
	
	add_to_order(request, slug)
	return redirect(request.META['HTTP_REFERER'])

