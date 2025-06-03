from rest_framework import status
from rest_framework import permissions, authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from catalog_app.fetchers import fetch_goods, fetch_categories
from catalog_app.serializers import GoodSerializer, CategorySerializer


class CategoryView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request: Request) -> Response:
        serializer = CategorySerializer(fetch_categories(), many=True)
        return Response(
            {"data": serializer.data, "errors": []},
            status=status.HTTP_200_OK,
        )

    def post(self, request: Request) -> Response:
        data = request.data.get("data")
        serializer = CategorySerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "data": serializer.data,
                    "errors": serializer.errors,
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {"data": None, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


class CatalogView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: Request) -> Response:
        serializer = GoodSerializer(fetch_goods(), many=True)
        return Response(
            {"data": serializer.data, "errors": []},
            status=status.HTTP_200_OK,
        )


class UploadCatalogView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request: Request) -> Response:
        data = request.data.get("data")
        serializer = GoodSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "data": serializer.data,
                    "errors": serializer.errors,
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {"data": None, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
