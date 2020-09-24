from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

from goodsapp.models import Good
from goodsapp.main import update_good
from .serializers import GoodSerializer


class ShowGoodsView(APIView):
    def get(self, request):
        goods = Good.objects.all()

        serializer = GoodSerializer(goods, many=True)
        return Response({"goods": serializer.data})


class UploadGoodsView(APIView):
    def post(self, request):

        goods = request.data.get('goods')
        # print()
        if goods is None:
            return Response({"success": "empty"})

        for good in goods:

           update_good(slug=good['slug'], name=good['name'], description=good['description'])
        return Response({"success": "ok"})
