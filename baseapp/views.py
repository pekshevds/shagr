from django.shortcuts import render

from shagr.core import get_context
from catalogapp.core import get_goods_for_carousel
from catalogapp.core import get_goods_for_new
from catalogapp.core import get_goods_for_sale
from catalogapp.core import get_goods_for_hot

from authapp.forms import ContactForm
from decouple import config
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


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

			# send_mail(name, phone, message)

			return render(request, 'baseapp/send_form_success.html', context)


def send_mail(name, phone, comment):

	HOST = "mail.hosting.reg.ru"
	sender_email = config('MAIL_USER')
	receiver_email = ['web@shagrbel.ru','mp1987@inbox.ru']
	password = config('MAIL_PASSWORD')

	message = MIMEMultipart("alternative")
	message["Subject"] = "Свяжитесь с {}. Контакты: {}".format(name, phone) 
	message["From"] = sender_email
	message["To"] = ','.join(receiver_email)

	text_body = """\
	"""

	html = """\
	<html>
      <body>
        <H3>Свяжитесь с {0}. Контакты: {1}</H3>
        <H3>Контакты:</H3>
        <p>Телефон: {1}</p>
        <p></p>
        <p>Комментарий:</p>
        <p>{2}</p>
      </body>
    </html>
	""".format(name, phone, comment)

	part1 = MIMEText(text_body, "plain")
	part2 = MIMEText(html, "html")
	message.attach(part1)
	message.attach(part2)

	context = ssl.create_default_context()

	server = smtplib.SMTP(HOST, 587)
	server.starttls()
	server.login(sender_email, password)
	server.sendmail(sender_email, receiver_email , message.as_string())
	server.quit()