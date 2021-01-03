from decimal import Decimal
from django.db.models import Avg, Max, Min, Count, Sum

from catalogapp.models import Good

from .models import Cart, CartItem




def get_cart(request):
	if request.user.is_authenticated:
		cart = get_cart_by_user(request.user)
	else:
		cart = get_cart_by_id(request.session.get('cart_id'))	

	request.session['cart_id'] = cart.id
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


def get_cart_by_user(user):
	try:
		cart = Cart.objects.get(user=user)
	except:
		cart = Cart.objects.create(user=user)

	return cart
	

def get_cart_by_id(id):
	try:
		cart = Cart.objects.get(id=id)
	except:
		cart = Cart.objects.create()	

	return cart