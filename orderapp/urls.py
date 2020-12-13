from django.urls import path

from .views import show_orders
from .views import show_order
from .views import del_good_from_order

from orderapp.views import add_good_to_order


urlpatterns = [

	path('', show_orders, name='show_orders'),
	path('order/<int:id>/', show_order, name='show_order'),
	path('del_from_order/<int:id>/', del_good_from_order, name='del_from_order'),
	path('add_to_order/<str:slug>/', add_good_to_order, name='add_to_order'),
]