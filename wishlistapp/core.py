from authapp.models import Buyer
from catalogapp.models import Good
from .models import WishList, WishListItem

from catalogapp.core import get_main_picture_of_good
from catalogapp.core import get_rating_of_good

def get_wishlist(request):
	
	if request.user.is_authenticated:
		wishlist = get_wishlist_by_user(request.user)
	else:
		wishlist = get_wishlist_by_id(request.session.get('wishlist_id'))	

	request.session['wishlist_id'] = wishlist['wishlist'].id
	return wishlist
	

def add_to_wishlist(wishlist, good):
			
	try:
		items = WishListItem.objects.filter(wishlist=wishlist['wishlist'], good=good)
	except:
		items = WishListItem.objects.create(wishlist=wishlist['wishlist'], good=good)

	if not items:
		items = WishListItem.objects.create(wishlist=wishlist['wishlist'], good=good)	


def del_from_wishlist(wishlist, good):
	
	try:
		WishListItem.objects.filter(wishlist=wishlist['wishlist'], good=good).delete()
	except:
		return False
	return True


def in_wishlist(wishlist, good):
	
	try:
		records = WishListItem.objects.filter(wishlist=wishlist['wishlist'], good=good)
	except:
		return False

	if records:
		return True
	return False

def get_count_wishlist(wishlist):
	
	try:
		records = WishListItem.objects.filter(wishlist=wishlist['wishlist'])
	except:
		return 0

	if records:
		return len(records)
	return 0

def get_wishlistitems(wishlist):
	
	try:
		records = WishListItem.objects.filter(wishlist=wishlist)
	except:
		records = None
	
	items = []
	goods = set()
	if records:
		for item in records:
			
			if not item.good in goods:
			
				items.append({
					'good'	: 	item.good,				
					'price'	: 	item.good.price,				
					'picture':	get_main_picture_of_good(item.good),
					'rating': 	get_rating_of_good(item.good),
					})
				goods.add(item.good)

	return items

def get_wishlist_by_user(user):

	try:
		wishlist = WishList.objects.get(user=user)
	except:
		wishlist = WishList.objects.create(user=user)

	items = get_wishlistitems(wishlist)

	
	return {
		'wishlist': wishlist,
		'items': items,
		'wishlist_count': len(items),
	}


def get_wishlist_by_id(id):

	try:
		wishlist = WishList.objects.get(id=id)
	except:
		wishlist = WishList.objects.create()

	items = get_wishlistitems(wishlist)

	
	return {
		'wishlist': wishlist,
		'items': items,
		'wishlist_count': len(items),
	}