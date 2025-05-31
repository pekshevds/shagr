from django.urls import path
from catalog_app.views import UploadCatalogView, CatalogView

app_name = "catalog"
urlpatterns = [
    path("catalog/", CatalogView.as_view(), name="show-catalog"),
    path("upload-catalog/", UploadCatalogView.as_view(), name="upload-catalog"),
]
