from authapp.models import Buyer
from catalogapp.models import Good
from .models import WishList, WishListItem


def get_wishlist(request):
	
	if request.user.is_authenticated:
		wishlist = get_wishlist_by_user(request.user)
	else:
		wishlist = get_wishlist_by_id(request.session.get('wishlist_id'))	

	request.session['wishlist_id'] = wishlist.id
	return wishlist
	

def add_to_wishlist(wishlist, good):
			
	try:
		items = WishListItem.objects.filter(wishlist=wishlist, good=good)
	except:
		items = WishListItem.objects.create(wishlist=wishlist, good=good)

	if not items:
		items = WishListItem.objects.create(wishlist=wishlist, good=good)	


def del_from_wishlist(wishlist, good):
	
	try:
		WishListItem.objects.filter(wishlist=wishlist, good=good).delete()
	except:
		return False
	return True


def clear_wishlist(wishlist):
	
	try:
		WishListItem.objects.filter(wishlist=wishlist).delete()
	except:
		return False
	return True


def get_wishlist_by_user(user):

	try:
		wishlist = WishList.objects.get(user=user)
	except:
		wishlist = WishList.objects.create(user=user)

	return wishlist


def get_wishlist_by_id(id):

	try:
		wishlist = WishList.objects.get(id=id)
	except:
		wishlist = WishList.objects.create()

	return wishlist