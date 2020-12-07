from django.shortcuts import render
from catalogapp.core import get_hierarchy_categoryes
from catalogapp.core import get_childs

# Create your views here.
def show_wishlist(request):
	childs = get_childs(parent=None)
	context = {
	'categories'			: get_hierarchy_categoryes(),
	'parent'				: None,
	'childs'				: childs,

	}
	return render(request, 'wishlistapp/wishlist.html', context)