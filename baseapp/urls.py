from django.urls import path, include
from .views import show_index
from .views import show_about
from .views import show_contacts
from .views import show_delivery
from .views import show_agreement
from .views import show_returns
from .views import show_map
from .views import show_brands
from .views import show_news

urlpatterns = [
    path('', show_index, name='show_index'),
    path('about/', show_about, name='about'),
    path('delivery/', show_delivery, name='delivery'),
    path('agreement/', show_agreement, name='agreement'),
    path('brands/', show_brands, name='brands'),
    path('contacts/', show_contacts, name='contacts'),
    path('returns/', show_returns, name='returns'),
    path('map/', show_map, name='map'),

    path('news/', show_news, name='news'),
]
