from django.shortcuts import render

from goodsapp.models import Category


def get_all_categories():

	category = Category.objects.all().order_by('-name')

	parents = []

	categories_with_parents = []

	categories_without_parents = []

	for cat in category:
		if cat.parent:
			if cat.parent not in parents:
				childs = list(Category.objects.filter(parent=cat.parent))
				categories_with_parents.append([cat.parent, childs])
				parents.append(cat.parent)

		else:
			categories_without_parents.append(cat)

	categories_with_parents.append(['Без категории', categories_without_parents[:10]])

	return categories_with_parents


def show_index(request):

	context = {

		'categories' : get_all_categories(),

	}
	
	return render(request, 'baseapp/index.html', context)
