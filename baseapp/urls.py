from django.urls import path
from .views import show_index

urlpatterns = [
    path('', show_index, name='show_index'),
]
