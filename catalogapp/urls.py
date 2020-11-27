from django.urls import path

from .views import show_catalog, show_list, show_item
 

urlpatterns = [

	path('', show_catalog, name='show_catalog'),
	path('category/<str:slug>/', show_list, name='show_list'),
	path('<str:slug>/', show_item, name='show_item'),

]