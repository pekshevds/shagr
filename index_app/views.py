from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.views import View
from django.http import HttpRequest, HttpResponse, Http404
from django.conf import settings
from catalog_app.fetchers import (
    fetch_good_by_id,
    fetch_category_by_id,
    fetch_goods,
    fetch_categories,
    fetch_goods_by_query,
    fetch_path,
)


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(
            request,
            template_name="index_app/index.html",
            context={
                "categories": fetch_categories(parent=None),
            },
        )


class CatalogView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        search = request.GET.get("search", "")
        if search:
            goods = fetch_goods_by_query(search)
        else:
            goods = fetch_goods()
        paginator = Paginator(goods, settings.PAGINATOR_ITEMS_ON_PAGE)
        page_obj = paginator.get_page(request.GET.get("page"))
        return render(
            request,
            template_name="index_app/catalog.html",
            context={
                "search": search,
                "goods": page_obj,
                "pages": range(1, page_obj.paginator.num_pages + 1),
                "categories": fetch_categories(parent=None),
            },
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        search = request.POST.get("search", "")
        return redirect(f"{reverse('index:catalog')}?search={search}&page=1")


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
        goods = fetch_goods(category)
        paginator = Paginator(goods, settings.PAGINATOR_ITEMS_ON_PAGE)
        page_obj = paginator.get_page(request.GET.get("page"))
        return render(
            request,
            template_name="index_app/catalog.html",
            context={
                "search": "",
                "goods": page_obj,
                "pages": range(1, page_obj.paginator.num_pages + 1),
                "categories": fetch_categories(parent=category),
                "category": category,
                "path": fetch_path(category),
            },
        )


class ContactView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, template_name="index_app/contact.html")
