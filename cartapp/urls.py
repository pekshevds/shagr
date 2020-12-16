from django.urls import path

from .views import show_cart
from .views import add_good_to_cart
from .views import insert_good_to_cart
from .views import del_good_from_cart
from .views import clear_current_cart

urlpatterns = [

	path('', show_cart, name='show_cart'),
	path('add_to_cart/<str:slug>/', add_good_to_cart, name='add_to_cart'),
	path('insert_to_cart/<str:slug>/', insert_good_to_cart, name='insert_to_cart'),
	path('del_from_cart/<str:slug>/', del_good_from_cart, name='del_from_cart'),
	path('clear_cart/', clear_current_cart, name='clear_cart'),
]