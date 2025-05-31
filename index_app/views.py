from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse, Http404
from catalog_app.fetchers import (
    fetch_good_by_id,
    fetch_category_by_id,
    fetch_goods,
    fetch_categories,
    fetch_goods_by_query,
)


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, template_name="index_app/index.html")


class CatalogView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        search = request.GET.get("search", "")
        if search:
            goods = fetch_goods_by_query(search)
        else:
            goods = fetch_goods()
        return render(
            request,
            template_name="index_app/catalog.html",
            context={
                "search": "",
                "goods": goods,
                "categories": fetch_categories(),
            },
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        search = request.POST.get("search", "")
        if search:
            goods = fetch_goods_by_query(search)
        else:
            goods = fetch_goods()
        return render(
            request,
            template_name="index_app/catalog.html",
            context={
                "search": search,
                "goods": goods,
                "categories": fetch_categories(),
            },
        )


class GoodView(View):
    def get(self, request: HttpRequest, id: str) -> HttpResponse:
        good = fetch_good_by_id(id)
        if not good:
            raise Http404("Товар не существует")
        return render(
            request,
            template_name="index_app/good.html",
            context={"good": good},
        )


class CategoryView(View):
    def get(self, request: HttpRequest, id: str) -> HttpResponse:
        category = fetch_category_by_id(id)
        if not category:
            raise Http404("Категория не существует")
        return render(
            request,
            template_name="index_app/catalog.html",
            context={"goods": fetch_goods(category), "categories": fetch_categories()},
        )


class ContactView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, template_name="index_app/contact.html")
