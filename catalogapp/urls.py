from django.urls import path

from .views import show_catalog
from .views import show_list
from .views import show_item
from .views import new_review
from .views import search

 

urlpatterns = [

	path('', show_catalog, name='show_catalog'),
	path('search/', search, name='search'),
	path('category/<str:slug>/', show_list, name='show_list'),	
	path('<str:slug>/', show_item, name='show_item'),
	path('new_review/<str:slug>/', new_review, name='new_review'),	
	
]