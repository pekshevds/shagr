from django.shortcuts import render

from shagr.core import get_context, send_mail
from catalogapp.core import get_goods_for_carousel
from catalogapp.core import get_goods_for_new
from catalogapp.core import get_goods_for_sale
from catalogapp.core import get_goods_for_hot

from authapp.forms import ContactForm


def show_index(request):
	context = get_context(request)
	context['carousel'] = get_goods_for_carousel()
	context['new_items'] = get_goods_for_new()
	context['sale_items'] = get_goods_for_sale()
	context['hot_items'] = get_goods_for_hot()

	return render(request, 'baseapp/index.html', context)

	# return show_catalog(request)

def show_about(request):
	context = get_context(request)
	return render(request, 'baseapp/about.html', context)

def show_contacts(request):
	context = get_context(request)
	return render(request, 'baseapp/contacts.html', context)

def show_delivery(request):
	context = get_context(request)
	return render(request, 'baseapp/delivery.html', context)

def show_agreement(request):
	context = get_context(request)
	return render(request, 'baseapp/agreement.html', context)

def show_returns(request):
	context = get_context(request)
	return render(request, 'baseapp/returns.html', context)

def show_map(request):
	context = get_context(request)
	return render(request, 'baseapp/map.html', context)

def show_brands(request):
	context = get_context(request)
	return render(request, 'baseapp/brands.html', context)

def show_news(request):
	context = get_context(request)
	return render(request, 'baseapp/news.html', context)

def send_contact_form(request):

	context = get_context(request)

	if request.method == 'POST':

		contactForm = ContactForm(request.POST)

		if contactForm.is_valid():

			name = contactForm.cleaned_data['contactName']
			phone = contactForm.cleaned_data['contactPhone']
			message = contactForm.cleaned_data['contactMessage']

			send_mail(name, phone, message)

			return render(request, 'baseapp/contact_form_success.html', context)

		else:

			return render(request, 'baseapp/contact_form_error.html', context)


