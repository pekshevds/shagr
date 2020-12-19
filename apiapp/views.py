from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

from catalogapp.models import Good
from catalogapp.models import Category
from catalogapp.core import update_good
from catalogapp.core import update_category

from catalogapp.tests import parse_categoryes
from catalogapp.tests import parse_goods

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
                            quant=good['quant'],
                            category_uid_1с=good['category_uid_1с'])

            parse_goods()
        except:
            return Response({"success": "error"})

        return Response({"success": "ok"})


# upload_categoryes/
class UploadCategoryesView(APIView):
    def post(self, request):

        categoryes = request.data.get('categoryes')

        if categoryes is None:
            return Response({"success": "categoryes list is none"})

        try:
            for category in categoryes:
                update_category(uid_1c=category['uid_1c'],                            
                            name=category['name'],
                            parent_uid_1c=category['parent_uid_1c'])

            parse_categoryes()
        except:
            return Response({"success": "error"})

        return Response({"success": "ok"})