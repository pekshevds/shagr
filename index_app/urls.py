from django.urls import path
from index_app.views import IndexView, CatalogView, GoodView, CategoryView, ContactView

app_name = "index"
urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("catalog/good/<str:id>/", GoodView.as_view(), name="good"),
    path("catalog/category/<str:id>/", CategoryView.as_view(), name="category"),
    path("catalog/", CatalogView.as_view(), name="catalog"),
    path("contacts/", ContactView.as_view(), name="contacts"),
]
