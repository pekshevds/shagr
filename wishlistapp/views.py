from django.shortcuts import render
from catalogapp.core import get_hierarchy_categoryes
from catalogapp.core import get_childs
from .core import get_wishlist_on_user
from .core import get_wishlist_on_id

# Create your views here.
def show_wishlist(request):
	
	if request.user.is_authenticated:
		wishlist = get_wishlist_on_user(request.user)
	else:
		wishlist = get_wishlist_on_id(request.session.get('wishlist_id'))	
	
	request.session['wishlist_id'] = wishlist['wishlist'].id

	childs = get_childs(parent=None)
	context = {
	'categories'			: get_hierarchy_categoryes(),
	'parent'				: None,
	'childs'				: childs,	
	'wishlist'				: wishlist,
	}
	return render(request, 'wishlistapp/wishlist.html', context)