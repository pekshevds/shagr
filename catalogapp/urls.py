from django.urls import path

from .views import show_catalog
from .views import show_list
from .views import show_item
from .views import new_review
from .views import add_to_card
from .views import add_to_wishlist
 

urlpatterns = [

	path('', show_catalog, name='show_catalog'),	
	path('category/<str:slug>/', show_list, name='show_list'),	
	path('<str:slug>/', show_item, name='show_item'),
	path('new_review/<str:slug>/', new_review, name='new_review'),
	path('add_to_card/<str:slug>/', add_to_card, name='add_to_card'),
	path('add_to_wishlist/<str:slug>/', add_to_wishlist, name='add_to_wishlist'),
]