from django.shortcuts import render

from catalogapp.views import show_catalog



def show_index(request):
		
	return show_catalog(request)
