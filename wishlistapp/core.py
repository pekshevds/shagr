from authapp.models import Buyer
from catalogapp.models import Good
from .models import WishList, Item

def get_wishlist_on_user(user):
	try:
		wishlist = WishList.objects.get(user=user)
	except:
		wishlist = WishList.objects.create(user=user)

	try:
		items = Item.objects.filter(wishlist=wishlist)
	except:
		items = None

	return {
		'wishlist': wishlist,
		'items': items,
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

	return {
		'wishlist': wishlist,
		'items': items,
	}


def add_to_wishlist_on_user(user, good):
	try:
		wishlist = WishList.objects.get(user=user)
	except:
		wishlist = WishList.objects.create(user=user)

	try:
		items = Item.objects.filter(wishlist=wishlist, good=good)
	except:
		items = Item.objects.create(wishlist=wishlist, good=good)

	if not items:
		items = Item.objects.create(wishlist=wishlist, good=good)


def add_to_wishlist_on_id(id, good):
	try:
		wishlist = WishList.objects.get(id=id)
	except:
		wishlist = WishList.objects.create(id=id)

	try:
		items = Item.objects.filter(wishlist=wishlist, good=good)
	except:
		items = Item.objects.create(wishlist=wishlist, good=good)

	if not items:
		items = Item.objects.create(wishlist=wishlist, good=good)


def del_from_wishlist(user, good):
	try:
		Item.objects.filter(buyer=user, good=good).delete()
	except:
		return False
	return True

def in_wishlist(user, good):
	try:
		records = Item.objects.filter(buyer=user, good=good)
	except:
		return False

	if records:
		return True
	return False