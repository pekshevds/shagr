from django.urls import path
from .views import show_card

urlpatterns = [

	path('', show_card, name='show_card'),
]