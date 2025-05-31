from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, template_name="index_app/index.html")


class CatalogView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(
            request,
            template_name="index_app/catalog.html",
            context={"range": range(100)},
        )


class ItemView(View):
    def get(self, request: HttpRequest, name: str) -> HttpResponse:
        return render(request, template_name="index_app/item.html")


class ContactView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, template_name="index_app/contact.html")
