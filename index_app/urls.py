from django.urls import path
from index_app.views import IndexView, CatalogView, ItemView, ContactView

app_name = "index"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("catalog/<str:name>/", ItemView.as_view(), name="item"),
    path("catalog/", CatalogView.as_view(), name="catalog"),
    path("contacts/", ContactView.as_view(), name="contacts"),
]
