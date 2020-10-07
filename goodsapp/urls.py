from django.urls import path

from .views import show_catalog, show_category
 

urlpatterns = [

	path('', show_catalog, name='show_catalog'),
	path('category/<str:slug>/', show_category, name='show_category'),

]
