from catalogapp.core import get_hierarchy_categoryes, get_main_categories
from catalogapp.core import get_childs
from catalogapp.core import get_brands


from cartapp.core import get_cart

from wishlistapp.core import get_wishlist

from authapp.core import get_buyer

import uuid
from decouple import config
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_uuid4():
    return str(uuid.uuid4())


def get_uuid():
    return str(uuid.uuid4().fields[0])


def get_context(request, parent=None):

	childs = get_childs(parent)
	

	context = {
	# 'categories'			: get_hierarchy_categoryes(),
	'main_categories'		: get_main_categories(),
	'parent'				: None,
	'childs'				: childs,		
	# 'brands'				: get_brands(parent),
	'cart'					: get_cart(request),
	'wishlist'				: get_wishlist(request),
	'buyer'					: get_buyer(request),
	}
	return context

def send_mail(name, phone, comment):

	HOST = "mail.hosting.reg.ru"
	sender_email = config('MAIL_USER')
	receiver_email = ['web@shagrbel.ru',]
	# receiver_email = ['info@annasoft.ru',]
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