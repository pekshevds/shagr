from django.urls import path
from .views import show_cart
from .views import add_good_to_cart
from .views import del_good_from_cart

urlpatterns = [

	path('', show_cart, name='show_cart'),
	path('add_to_cart/<str:slug>/', add_good_to_cart, name='add_to_cart'),
	path('del_from_cart/<str:slug>/', del_good_from_cart, name='del_from_cart'),
]