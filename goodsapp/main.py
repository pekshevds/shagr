from .models import Good


def create_good(slug, name, art='', full_name='', description='', is_sale=False, is_new=False, is_hot=False):

    good = find_good_by_slug(slug)
    if not good is None:
        return good

    try:

        good = Good.objects.create(slug=slug, name=name, art=art, full_name=full_name, description=description, is_sale=is_sale, is_new=is_new, is_hot=is_hot)
        # good.save()

    except:
        return None
    return good

def update_good(slug, name, art='', full_name='', description='', is_sale=False, is_new=False, is_hot=False):

    good = find_good_by_slug(slug)
    if good is None:
        return create_good(slug=slug, name=name, art=art, full_name=full_name, description=description, is_sale=is_sale, is_new=is_new, is_hot=is_hot)

    try:

        good.name=name,
        good.art=art
        good.full_name=full_name
        good.description=description
        good.is_sale=is_sale
        good.is_new=is_new
        good.is_hot=is_hot
        good.save()

    except:
        return good
    return good

def find_good_by_slug(slug):
    try:
        return Good.objects.get(slug=slug)
    except:
        return None
