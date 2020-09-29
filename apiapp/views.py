from _ast import excepthandler

from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

from goodsapp.models import Good
from goodsapp.main import update_good, download_offer
from .serializers import GoodSerializer


# download_goods/
class DownloadGoodsView(APIView):
    def get(self, request):
        goods = Good.objects.all()

        serializer = GoodSerializer(goods, many=True)
        return Response({"goods": serializer.data})


# upload_goods/
class UploadGoodsView(APIView):
    def post(self, request):

        goods = request.data.get('goods')

        if goods is None:
            return Response({"success": "goods list is none"})

        try:
            for good in goods:
                update_good(uid_1c=good['uid_1c'],
                            name=good['name'],
                            art=good['art'],
                            description=good['description'],
                            full_name=good['full_name'])
        except:
            return Response({"success": "error"})

        return Response({"success": "ok"})


# upload_offers/
class UploadOffersView(APIView):
    def post(self, request):

        offers = request.data.get('offers')

        if offers is None:
            return Response({"success": "offers list is none"})

        try:
            for offer in offers:
                download_offer(uid_1c=offer['uid_1c'],
                             price=offer['price'],
                             quant=offer['quant'])
        except:
            return Response({"success": "error"})

        return Response({"success": "ok"})
