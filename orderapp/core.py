from decimal import Decimal

from .models import Order
from .models import OrderItem

from catalogapp.core import find_good_by_slug
from authapp.core import get_buyer
from cartapp.core import get_cart


def get_orders(buyer):

	return Order.objects.filter(buyer=buyer).order_by('-date')


def get_order(id):	
	try:
		order = Order.objects.get(id=id)
	except:
		return None

	return order


def del_from_order(id):
	try:
		item = OrderItem.objects.get(id=id)
	except:
		return False

	order = item.order
	
	item.delete()
	order.save()
	return True

	
def reprice_order(order):
	
	items = order.get_items()
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
		quant = Decimal(request.POST.get('quant', 1))
		price = Decimal(request.POST.get('price', 0))
		total = Decimal(request.POST.get('total', 0))

		order = get_current_order(request)
		items = OrderItem.objects.filter(order=order, good=good)		
		if items:

			item = items[0]
			item.quant = item.quant + quant
			item.save()
		else:
			items = OrderItem.objects.create(order=order, good=good, quant=quant)

		order.save()


def create_order_from_cart(request):

	cart = get_cart(request)
	
	buyer = get_buyer(request)
	order = Order.objects.create(buyer=buyer)

	cartitems = cart.get_items()
	if cartitems:
		for item in cartitems:
			OrderItem.objects.create(order=order, good=item.good, quant=item.quant)	
	
		order.save()

		cart.clear()
		return order
	return None


def change_payment_status_of_order(id, payment_status='AP'):
	try:
		order = get_order(id=id)
	except:
		return False	
	
	order.payment_status = payment_status
	order.delivery_status = 'GT'
	order.save()
	return True