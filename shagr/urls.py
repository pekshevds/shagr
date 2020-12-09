from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('', include('baseapp.urls')),
    path('catalog/', include('catalogapp.urls')),
    path('api/', include('apiapp.urls')),
    path('accounts/', include('authapp.urls')),
    path('wistlist/', include('wishlistapp.urls')),
    path('cart/', include('cartapp.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()