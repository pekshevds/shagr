from django.urls import path, include
from .views import DownloadGoodsView, UploadGoodsView

urlpatterns = [
	path('download_goods/', DownloadGoodsView.as_view()),
	path('upload_goods/', UploadGoodsView.as_view()),	
	# path('download_orders/', GoodView.as_view()),
]
