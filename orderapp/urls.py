from django.urls import path

from .views import show_orders
from .views import show_order
from .views import del_good_from_order
from .views import send_cart_to_order
from .views import pay_for_order

from orderapp.views import add_good_to_order


urlpatterns = [

	path('', show_orders, name='show_orders'),
	path('send_cart_to_order/', send_cart_to_order, name='send_cart_to_order'),
	path('pay_for_order/<int:id>/', pay_for_order, name='pay_for_order'),
	path('order/<int:id>/', show_order, name='show_order'),
	path('del_from_order/<int:id>/', del_good_from_order, name='del_from_order'),
	path('add_to_order/<str:slug>/', add_good_to_order, name='add_to_order'),
]