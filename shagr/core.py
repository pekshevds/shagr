from catalogapp.core import get_hierarchy_categoryes
from catalogapp.core import get_childs

from cartapp.core import get_cart

from wishlistapp.core import get_wishlist

from authapp.core import get_buyer

import uuid

def get_uuid4():
    return str(uuid.uuid4())


def get_uuid():
    return str(uuid.uuid4().fields[0])


def get_context(request):

	childs = get_childs(parent=None)
	

	context = {
	'categories'			: get_hierarchy_categoryes(),
	'parent'				: None,
	'childs'				: childs,		
	'cart'					: get_cart(request),
	'wishlist'				: get_wishlist(request),
	'buyer'					: get_buyer(request),
	}
	return context