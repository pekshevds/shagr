from django.shortcuts import render, redirect
from catalogapp.core import find_good_by_slug

# Create your views here.
def show_card(request):
	pass

def add_good_to_card(request, slug):

	try:
		quant = request.POST['quant']
	except:
		quant = 1
	
	good = find_good_by_slug(slug=slug)
	if good:
		parent = good.category
	return redirect(request.META['HTTP_REFERER'])

