from django.shortcuts import render

from goodsapp.models import Category


def get_childs(parent=None):

	childs = Category.objects.filter(parent=parent).order_by('-name')

	return childs


def get_all_categoryes(parent=None):

	categoryes = Category.objects.all().order_by('-name')

	parents_not_for_menu = []

	parents = []

	categoryes_with_parents = []

	categoryes_without_parents = []

	for category in categoryes:

		if category.parent:

			if category.parent not in parents:

				parents.append(category.parent)

				childs = list(get_childs(category.parent))

				temp = []

				for ch in childs:

					child_of_child = list(get_childs(ch))

					temp.append([ch, child_of_child])

					if ch not in parents_not_for_menu:
						parents_not_for_menu.append(ch)

				categoryes_with_parents.append([category.parent, temp])

		else:
			categoryes_without_parents.append(category)

	temp1 = []	
	for category in categoryes_without_parents:

		#child_of_child = list(get_childs(ch))
		child_of_child = list(get_childs(category))

		temp1.append([category, child_of_child])

	categoryes_with_parents.append(['Без категории', temp1 ])

	return [categoryes_with_parents, parents_not_for_menu]


def show_index(request):

	context = {

		'categories' : get_all_categoryes(),

	}
	
	return render(request, 'baseapp/index.html', context)
