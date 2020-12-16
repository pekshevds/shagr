from decimal import Decimal
from django.db.models import Avg, Max, Min, Count, Sum

from catalogapp.models import Good
from catalogapp.core import get_main_picture_of_good
from catalogapp.core import get_rating_of_good

from .models import Cart, CartItem




def get_cart(request):
	if request.user.is_authenticated:
		cart = get_cart_by_user(request.user)
	else:
		cart = get_cart_by_id(request.session.get('cart_id'))	

	request.session['cart_id'] = cart['cart'].id
	return cart
	

def add_to_cart(cart, good, quant=1):

	items = CartItem.objects.filter(cart=cart, good=good)
	if items:

		item = items[0]
		item.quant = item.quant + quant
		item.save()
	else:
		items = CartItem.objects.create(cart=cart, good=good, quant=quant)	


def insert_to_cart(cart, good, quant=1):

	CartItem.objects.filter(cart=cart, good=good).delete()	
	CartItem.objects.create(cart=cart, good=good, quant=quant)


def del_from_cart(cart, good):
	
	try:
		CartItem.objects.filter(cart=cart, good=good).delete()
	except:
		return False
	return True


def clear_cart(cart):
	
	try:
		CartItem.objects.filter(cart=cart).delete()
	except:
		return False
	return True


def in_cart(cart, good):

	try:
		records = CartItem.objects.filter(cart=cart, good=good)
	except:
		return False

	if records:
		return True
	return False


def get_sum_cart(cart):
	return cart['cart_sum']


def get_cartitems(cart):
	
	try:
		records = CartItem.objects.filter(cart=cart).values('good').annotate(quant=Sum('quant'))
	except:
		records = None
	
	items = []
	if records:
		for item in records:
			
			good = Good.objects.get(id=item['good'])
			quant = Decimal((item['quant']))

			items.append({
				'good'	: 	good,
				'quant'	: 	quant,
				'price'	: 	good.price,
				'sum'	: 	round(good.price * quant, 2),
				'picture':	get_main_picture_of_good(good),
				'rating': 	get_rating_of_good(good),
				})

	return items


def init_cart(cart):

	cart_sum = 0
	cart_quant = 0
	
	items = get_cartitems(cart)
	for item in items:
		cart_sum = cart_sum + item['sum']
		cart_quant = cart_quant + item['quant']
		

	return {
		'cart'		: cart,
		'items'		: items,
		'cart_sum'	: cart_sum,
		'cart_quant': cart_quant,
	}

def get_cart_by_user(user):
	try:
		cart = Cart.objects.get(user=user)
	except:
		cart = Cart.objects.create(user=user)

	return init_cart(cart)
	


def get_cart_by_id(id):
	try:
		cart = Cart.objects.get(id=id)
	except:
		cart = Cart.objects.create()	

	return init_cart(cart)