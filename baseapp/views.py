from django.shortcuts import render

from goodsapp.models import Category


def get_childs(parent=None):

	childs = Category.objects.filter(parent=parent).order_by('-name')

	return childs


def get_all_categories(parent=None):

	category = Category.objects.all().order_by('-name')

	parents_not_for_menu = []

	parents = []

	categories_with_parents = []

	categories_without_parents = []

	for cat in category:

		if cat.parent:

			if cat.parent not in parents:

				parents.append(cat.parent)

				childs = list(get_childs(cat.parent))

				temp = []

				for ch in childs:

					child_of_child = list(get_childs(ch))

					temp.append([ch, child_of_child])

					if ch not in parents_not_for_menu:
						parents_not_for_menu.append(ch)

				categories_with_parents.append([cat.parent, temp])

		else:
			categories_without_parents.append(cat)

	temp1 = []

	for cat in categories_without_parents[:10]:

		child_of_child = list(get_childs(ch))

		temp1.append([cat, child_of_child])

	categories_with_parents.append(['Без категории', temp1 ])

	return [categories_with_parents, parents_not_for_menu]


def show_index(request):

	context = {

		'categories' : get_all_categories(),

	}
	
	return render(request, 'baseapp/index.html', context)
