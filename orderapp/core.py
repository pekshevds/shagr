from .models import Order
from .models import OrderItem

from catalogapp.core import get_rating_of_good
from catalogapp.core import get_main_picture_of_good
from catalogapp.core import find_good_by_slug

from authapp.core import get_buyer


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

	items = []
	for orderItem in OrderItem.objects.filter(order=order):
		items.append({
			'id': orderItem.id,
			'good': orderItem.good,
			'quant': orderItem.quant,
			'price': orderItem.price,
			'total': orderItem.total,
			'rating': get_rating_of_good(good=orderItem.good),
			'picture': get_main_picture_of_good(good=orderItem.good),
			})

	context['order'] = order
	context['items'] = items

	return context

def del_from_order(id):
	OrderItem.objects.filter(id=id).delete()

def reprice_order(order):
	
	items = OrderItem.objects.filter(order=order)
	for item in item:
		item.price = item.good.price
		item.save()

	order.save()


def get_current_order(request):
	buyer = get_buyer(request)
	orders = Order.objects.filter(buyer=buyer, payment_status="NP", delivery_status="AW")
	if orders:
		return orders[0]

	return Order.objects.create(buyer=buyer)


def add_to_order(request, slug):

	good = find_good_by_slug(slug=slug)
	
	if good and request.method == 'POST':
		quant = float(request.POST.get('quant', 1))
		price = float(request.POST.get('price', 0))
		total = float(request.POST.get('total', 0))

		order = get_current_order(request)
		items = OrderItem.objects.filter(order=order, good=good)		
		if items:

			item = items[0]
			item.quant = item.quant + quant
			item.save()
		else:
			items = OrderItem.objects.create(order=order, good=good, quant=quant)

