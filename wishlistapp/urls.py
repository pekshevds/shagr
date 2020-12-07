from django.urls import path
from .views import show_wishlist

urlpatterns = [

	path('', show_wishlist, name='show_wishlist'),
]