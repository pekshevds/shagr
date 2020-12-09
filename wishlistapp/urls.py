from django.urls import path
from .views import show_wishlist
from .views import add_good_to_wishlist
from .views import del_good_from_wishlist

urlpatterns = [

	path('', show_wishlist, name='show_wishlist'),
	path('add_to_wishlist/<str:slug>/', add_good_to_wishlist, name='add_to_wishlist'),
	path('del_from_wishlist/<str:slug>/', del_good_from_wishlist, name='del_from_wishlist'),
]