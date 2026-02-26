from django.db.models import QuerySet, Q
from catalog_app.models import Good, Category, PropertyItem


def fetch_good_by_id(id: str) -> Good | None:
    return Good.active_items.filter(id=id).first()


def fetch_goods(category: Category | None = None) -> QuerySet:
    if category:
        return category.goods.all().order_by("name")
    return Good.active_items.all().order_by("name")


def fetch_properties(good: Good) -> QuerySet:
    return PropertyItem.objects.filter(good=good).all()


def fetch_categories(parent: Category | None = None) -> QuerySet:
    return Category.objects.filter(parent=parent).order_by("name")


def fetch_path(category: Category) -> list[Category]:
    category_list = []
    parent = category.parent
    while True:
        if parent is None:
            break
        category_list.append(parent)
        parent = parent.parent
    category_list.reverse()
    return category_list


def fetch_goods_by_query(query: str) -> QuerySet:
    return (
        Good.active_items.filter(
            Q(name__icontains=query)
            | Q(art__icontains=query)
            | Q(full_name__icontains=query)
            | Q(description__icontains=query)
        )
        .all()
        .order_by("name")
    )


def fetch_category_by_id(id: str) -> Category | None:
    return Category.objects.filter(id=id).first()
