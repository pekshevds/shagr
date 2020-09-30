from django.urls import path
from .views import show_index

urlpatterns = [
    path('', show_index, name='index_page'),
]
