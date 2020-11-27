from .models import Good
from .models import Offer
from .models import GoodsPropertyValue
from .models import Category


# universal
def find_good_by_uid_1c(uid_1c):
    try:
        good = Good.objects.get(uid_1c=uid_1c)
    except:
        return None

    return good


def find_category_by_name(name):
    try:
        category = Category.objects.get(name=name)
    except:
        return None

    return category


def find_category_by_slug(slug):
    parents = Category.objects.filter(slug=slug)

    parent = None
    
    if parents:
        parent = parents[0]
    return parent

def find_good_by_slug(slug):
    goods = Good.objects.filter(slug=slug)

    good = None
    
    if goods:
        good = goods[0]
    return good



# category
def create_category(name, uid_1c='', parent_uid_1c=''):
    category = find_category_by_name(name)

    if not category is None:
        return category

    try:

        category = Category.objects.create(name=name, uid_1c=uid_1c, parent_uid_1c=parent_uid_1c)    

    except:
        return None
    return category

# goods
def create_good(uid_1c, name,
                art='', code_1c='',
                description='', is_sale=False,
                is_new=False, is_hot=False, is_service=False):#, category=''):

    good = find_good_by_uid_1c(uid_1c)
    if not good is None:
        return good

    try:

        good = Good.objects.create(uid_1c=uid_1c, name=name,
                                   art=art, code_1c=code_1c,
                                   description=description, is_sale=is_sale,
                                   is_new=is_new, is_hot=is_hot, is_service=is_service,)# category=create_category(name=category))
        # good.save()

    except:
        return None
    return good


def update_good(uid_1c, name, art='',
                code_1c='', description='',
                is_sale=False, is_new=False,
                is_hot=False, is_service=False):#, category=''):

    good = find_good_by_uid_1c(uid_1c)
    if good is None:
        return create_good(uid_1c=uid_1c, name=name,
                           art=art, code_1c=code_1c,
                           description=description, is_sale=is_sale,
                           is_new=True, is_hot=is_hot, is_service=is_service)#, category=category)

    try:

        good.name = name
        good.code_1c = code_1c
        good.art = art
        good.description = description
        good.is_sale = is_sale
        good.is_new = is_new
        good.is_hot = is_hot
        good.is_service = is_service
        #good.category = create_category(name=category)
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
def download_offer(uid_1c, price=0, quant=0):
    good = find_good_by_uid_1c(uid_1c)

    if good is None:
        return None

    try:
        offer = create_offer(good=good, price=price, quant=quant)
    except:
        return None
    return offer


def create_offer(good, price=0, quant=0):
    if good is None:
        return None
    
    try:
        offer = Offer.objects.create(good=good, price=price, quant=quant)
    except:
        return None
    return offer


def get_last_offer(good):
    try:
        offer = Offer.objects.filter(good=good).order_by('-date')[:0]
    except:
        return None
    return offer













def get_childs(parent=None):

    childs = Category.objects.filter(parent=parent).order_by('name')

    return childs

def get_goods(category=None):

    goods = Good.objects.filter(category=category).order_by('name')

    return goods


def get_layer(parent=None):
    c = {}
    childs = get_childs(parent)

    if childs:

        for layer in childs:
            c[layer] = get_layer(layer)

        return c

    return None


def get_hierarchy_categoryes():

    c0 = get_layer()
    return c0




