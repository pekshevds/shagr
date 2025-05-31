from django.db.models import QuerySet
from catalog_app.models import Good, Category


def fetch_good_by_id(id: str) -> Good | None:
    return Good.active_items.filter(id=id).first()


def fetch_goods(category: Category | None = None) -> QuerySet:
    if category:
        return category.goods.all()
    return Good.active_items.all()


def fetch_category_by_id(id: str) -> Category | None:
    return Category.objects.filter(id=id).first()


def fetch_categories() -> QuerySet:
    return Category.objects.all()
