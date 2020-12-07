from authapp.models import Buyer
from catalogapp.models import Good
from .models import Item

def get_wishlist(user):
	try:
		records = Item.objects.filter(buyer=user)
	except:
		return None
	return records


def add_to_wishlist(user, good):
	try:
		Item.objects.create(buyer=user, good=good)
	except :
		return False
	return True

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