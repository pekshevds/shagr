from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

from catalogapp.models import Good
from catalogapp.core import update_good
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
                            code_1c=good['code_1c'],
                            name=good['name'],
                            art=good['art'],
                            description=good['description'],
                            is_service=good['is_service'] == "True",
                            price=good['price'],
                            quant=good['quant'])
        except:
            return Response({"success": "error"})

        return Response({"success": "ok"})