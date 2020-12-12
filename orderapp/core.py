from .models import Order
from .models import OrderItem

def get_orders(buyer):

	return Order.objects.filter(buyer=buyer)

def get_order(id):
	
	context = {
		'order': None,
		'items': [],
	}

	order = None
	try:
		order = Order.objects.get(id=id)
	except:
		return context

	items = list(OrderItem.objects.filter(order=order))
	context['order'] = order
	context['items'] = items

	return context


