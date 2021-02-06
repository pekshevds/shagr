from .models import Good
from .models import Picture
from .models import GoodsPropertyValue
from .models import Category
from .models import Review
from .models import Brand

# universal
def find_good_by_uid_1c(uid_1c):
    try:
        good = Good.objects.get(uid_1c=uid_1c)
    except:
        return None

    return good


def find_category_by_uid_1c(uid_1c):
    try:
        category = Category.objects.get(uid_1c=uid_1c)
    except:
        return None

    return category


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


# goods
def create_good(uid_1c, name,
                art='', code_1c='',
                description='', is_sale=False,
                is_new=False, is_hot=False, is_service=False,
                price=0, quant=0, category_uid_1с=''):#, category=''):

    good = find_good_by_uid_1c(uid_1c)
    if good:
        return good
    try:

        good = Good.objects.create(uid_1c=uid_1c, name=name,
                                   art=art, code_1c=code_1c,
                                   description=description, is_sale=is_sale,
                                   is_new=is_new, is_hot=is_hot, is_service=is_service,
                                   price=price, quant=quant, category_uid_1с=category_uid_1с)# category=create_category(name=category))
        # good.save()

    except:
        return None
    return good


def update_good(uid_1c, name, art='',
                code_1c='', description='',
                is_sale=False, is_new=False,
                is_hot=False, is_service=False,
                price=0, quant=0, category_uid_1с=''):

    good = find_good_by_uid_1c(uid_1c)
    if good:
        try:            
            good.name = name
            good.code_1c = code_1c
            good.art = art
            good.description = description
            good.is_sale = is_sale
            good.is_new = is_new
            good.is_hot = is_hot
            good.is_service = is_service
            good.price = price
            good.quant = quant
            good.is_show = (quant > 0)
            good.category_uid_1с = category_uid_1с
            good.category = find_category_by_uid_1c(uid_1c=good.category_uid_1с)
            good.save()

        except:            
            return good
        
        
    else:
        good = create_good(uid_1c=uid_1c, name=name,
                           art=art, code_1c=code_1c,
                           description=description, is_sale=is_sale,
                           is_new=True, is_hot=is_hot, is_service=is_service,
                           price=price, quant=quant, category_uid_1с=category_uid_1с)
        if good:
            good.category = find_category_by_uid_1c(uid_1c=good.category_uid_1с)
            good.save()
        
    return good


def create_category(uid_1c, name,
                parent_uid_1c=''):

    category = find_category_by_uid_1c(uid_1c)
    if category:
        return category
    try:
        category = Category.objects.create(uid_1c=uid_1c, name=name,
                                   parent_uid_1c=parent_uid_1c)        

    except:
        return None
    return category


def update_category(uid_1c, name, parent_uid_1c=''):

    category = find_category_by_uid_1c(uid_1c)
    if category:
        try:

            category.name = name
            category.uid_1c = uid_1c
            category.parent_uid_1c=parent_uid_1c      
            category.save()

        except:
            pass
        return category
    else:
        return create_category(uid_1c=uid_1c, name=name,
                           parent_uid_1c=parent_uid_1c)    


def get_category_goods(category_list):
    try:
        goods = Good.objects.filter(category__in=category_list)
    except:
        return None

    if goods:        
        return goods

    return None


def get_childs(parent=None):

    childs = Category.objects.filter(parent=parent).order_by('name')

    return childs


def get_goods(category=None):

    goods = Good.objects.filter(category=category).order_by('name')

    return goods


def get_search(name=""):

    goods = Good.objects.filter(name__icontains=name)

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


def add_review(user, slug, rating, review):
    good = find_good_by_slug(slug)
    if good:
        try:
            new_review = Review.objects.create(user=user, good=good, review=review, rating=rating)
        except:
            return False        
    else:
        return False
    return True


def get_brands():
    
    brands = Brand.objects.all()
    return brands