from django.urls import path, include
from .views import DownloadGoodsView
from .views import UploadGoodsView
from .views import UploadCategoryesView

urlpatterns = [
	path('download_goods/', DownloadGoodsView.as_view()),
	path('upload_goods/', UploadGoodsView.as_view()),
	path('upload_categoryes/', UploadCategoryesView.as_view()),
	# path('download_orders/', GoodView.as_view()),
]
