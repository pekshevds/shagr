from authapp.models import Buyer
from catalogapp.models import Good
from .models import WishList, Item



def get_wishlist(request):
	if request.user.is_authenticated:
		wishlist = get_wishlist_on_user(request.user)
	else:
		wishlist = get_wishlist_on_id(request.session.get('wishlist_id'))	

	request.session['wishlist_id'] = wishlist['wishlist'].id
	return wishlist
	

def add_to_wishlist(request, good):
	
	wishlist = get_wishlist(request)
	
	try:
		items = Item.objects.filter(wishlist=wishlist['wishlist'], good=good)
	except:
		items = Item.objects.create(wishlist=wishlist['wishlist'], good=good)

	if not items:
		items = Item.objects.create(wishlist=wishlist['wishlist'], good=good)	


def del_from_wishlist(request, good):
	
	wishlist = get_wishlist(request)	

	try:
		Item.objects.filter(wishlist=wishlist['wishlist'], good=good).delete()
	except:
		return False
	return True


def in_wishlist(request, good):

	wishlist = get_wishlist(request)

	try:
		records = Item.objects.filter(wishlist=wishlist['wishlist'], good=good)
	except:
		return False

	if records:
		return True
	return False

def get_count_wishlist(request):

	wishlist = get_wishlist(request)

	try:
		records = Item.objects.filter(wishlist=wishlist['wishlist'])
	except:
		return 0

	if records:
		return len(records)
	return 0


def get_wishlist_on_user(user):
	try:
		wishlist = WishList.objects.get(user=user)
	except:
		wishlist = WishList.objects.create(user=user)

	try:
		items = Item.objects.filter(wishlist=wishlist)
	except:
		items = None

	goods = set()
	for item in items:
		goods.add(item.good)

	return {
		'wishlist': wishlist,
		'goods': list(goods),
	}


def get_wishlist_on_id(id):
	try:
		wishlist = WishList.objects.get(id=id)
	except:
		wishlist = WishList.objects.create()

	try:
		items = Item.objects.filter(wishlist=wishlist)
	except:
		items = None

	goods = set()
	for item in items:
		goods.add(item.good)

	return {
		'wishlist': wishlist,
		'goods': list(goods),
	}