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
	

def add_to_cart(request, good, quant=1):
	
	cart = get_cart(request)
		
	items = CartItem.objects.create(cart=cart['cart'], good=good, quant=quant)	


def del_from_cart(request, good):
	
	cart = get_cart(request)	

	try:
		CartItem.objects.filter(cart=cart['cart'], good=good).delete()
	except:
		return False
	return True


def in_cart(request, good):

	cart = get_cart(request)

	try:
		records = CartItem.objects.filter(cart=cart['cart'], good=good)
	except:
		return False

	if records:
		return True
	return False


def get_count_cart(request):

	cart = get_cart(request)

	try:
		records = CartItem.objects.filter(cart=cart['cart'])
	except:
		return 0

	if records:
		return len(records)
	return 0


def get_sum_cart(request):
	return get_cart(request)['cart_sum']


def get_cartitems(cart):

	try:
		cartitems = CartItem.objects.filter(cart=cart)
	except:
		cartitems = None

	items = []
	for item in cartitems:
		items.append({
			'good'	:item.good,
			'quant'	:item.quant,
			'price'	: 0,
			'sum'	: 0,
			'picture': get_main_picture_of_good(item.good),            
            'rating': get_rating_of_good(item.good),
			})
	return items


def get_cart_by_user(user):
	try:
		cart = Cart.objects.get(user=user)
	except:
		cart = Cart.objects.create(user=user)

	cart_sum = 0
	items = get_cartitems(cart)
	for item in items:
		cart_sum = cart_sum + item['sum']

	return {
		'cart'		: cart,
		'items'		: items,
		'cart_sum'	: cart_sum,
	}


def get_cart_by_id(id):
	try:
		cart = Cart.objects.get(id=id)
	except:
		cart = Cart.objects.create()	

	cart_sum = 0
	items = get_cartitems(cart)
	for item in items:
		cart_sum = cart_sum + item['sum']

	return {
		'cart'		: cart,
		'items'		: items,
		'cart_sum'	: cart_sum,
	}