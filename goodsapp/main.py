from .models import Good
from .models import Offer
from .models import GoodsPropertyValue


# universal
def find_good_by_slug(slug):
    try:
        good = Good.objects.get(slug=slug)
    except:
        return None

    return good


# goods
def create_good(slug, name, art='', full_name='', description='', is_sale=False, is_new=False, is_hot=False):
    good = find_good_by_slug(slug)
    if not good is None:
        return good

    try:

        good = Good.objects.create(slug=slug, name=name, art=art, full_name=full_name, description=description,
                                   is_sale=is_sale, is_new=is_new, is_hot=is_hot)
        # good.save()

    except:
        return None
    return good


def update_good(slug, name, art='', full_name='', description='', is_sale=False, is_new=False, is_hot=False):
    good = find_good_by_slug(slug)
    if good is None:
        return create_good(slug=slug, name=name, art=art, full_name=full_name, description=description, is_sale=is_sale,
                           is_new=is_new, is_hot=is_hot)

    try:

        good.name = name,
        good.art = art
        good.full_name = full_name
        good.description = description
        good.is_sale = is_sale
        good.is_new = is_new
        good.is_hot = is_hot
        good.save()

    except:
        return good
    return good


def get_properties_and_values(good):
    try:
        records = GoodsPropertyValue.objects.filter(good=good)
    except:
        return None
    return records


def get_category_goods(category_list):
    try:
        goods = Good.objects.filter(category__in=category_list)
    except:
        return None
    return goods










# offers
def create_offer(slug, price=0, quant=0):
    good = find_good_by_slug(slug)
    if good is None:
        return None

    try:
        offer = Offer.objects.create(good, price, quant)
    except:
        return None
    return offer


def get_last_offer(good):
    try:
        offer = Offer.objects.filter(good=good).order_by('-date')[:0]
    except:
        return None
    return offer