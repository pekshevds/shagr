from django.urls import path
from .views import show_orders
from .views import show_order


urlpatterns = [

	path('', show_orders, name='show_orders'),
	path('order/<int:id>/', show_order, name='show_order'),
]