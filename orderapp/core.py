from decimal import Decimal

from .models import Order
from .models import OrderItem

from catalogapp.core import find_good_by_slug
from authapp.core import get_buyer
from cartapp.core import get_cart

from decouple import config
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_orders(buyer):

	return Order.objects.filter(buyer=buyer).order_by('-date')


def get_order(id):	
	try:
		order = Order.objects.get(id=id)
	except:
		return None

	return order


def del_from_order(id):
	try:
		item = OrderItem.objects.get(id=id)
	except:
		return False

	order = item.order
	
	item.delete()
	order.save()
	return True

	
def reprice_order(order):
	
	items = order.get_items()
	for item in item:
		item.price = item.good.price
		item.save()

	order.save()


def get_current_order(request):
	buyer = get_buyer(request)
	orders = Order.objects.filter(buyer=buyer, payment_status="NP", delivery_status="AW")
	if orders:
		return orders[0]

	return Order.objects.create(buyer=buyer)


def add_to_order(request, slug):

	good = find_good_by_slug(slug=slug)
	
	if good and request.method == 'POST':
		quant = Decimal(request.POST.get('quant', 1))
		price = Decimal(request.POST.get('price', 0))
		total = Decimal(request.POST.get('total', 0))

		order = get_current_order(request)
		items = OrderItem.objects.filter(order=order, good=good)		
		if items:

			item = items[0]
			item.quant = item.quant + quant
			item.save()
		else:
			items = OrderItem.objects.create(order=order, good=good, quant=quant)

		order.save()


def create_order_from_cart(request):

	cart = get_cart(request)
	
	buyer = get_buyer(request)
	order = Order.objects.create(buyer=buyer)

	cartitems = cart.get_items()
	if cartitems:
		for item in cartitems:
			OrderItem.objects.create(order=order, good=item.good, quant=item.quant)	
	
		order.save()

		cart.clear()
		return order
	return None


def change_payment_status_of_order(id, payment_status='AP'):
	try:
		order = get_order(id=id)
	except:
		return False	
	
	order.payment_status = payment_status
	order.delivery_status = 'GT'
	order.save()
	return True

def send_mail_with_order(order):

	HOST = "mail.hosting.reg.ru"
	sender_email = config('MAIL_USER')
	receiver_email = ['web@shagrbel.ru',]
	# receiver_email = ['info@annasoft.ru',]
	password = config('MAIL_PASSWORD')

	message = MIMEMultipart("alternative")
	message["Subject"] = "Поступил заказ № {} от {}".format(order.id, order.date.strftime("%Y-%m-%d")) 
	message["From"] = sender_email
	message["To"] = ','.join(receiver_email)

	order_items = ""

	css_style_td = """\
	style="border-bottom: 1px solid #ececec; padding: 14px 0; text-align: center;"
	"""

	if order:
		for item in OrderItem.objects.filter(order=order):
			order_items += "<tr><td {3}>{0}</td> <td {3}>x{1}</td> <td{3}>{2}</td></tr>".format(item.good, item.quant, item.total, css_style_td)

		text = """\
		{}""".format(order_items)


		html = """\
	    <html>
	      <body>
	      <div style="max-width: 610px; width:100%">
	        <H4 style="background-color: #0064f0; color: #fff; padding: 12px 0; text-align: center; font-size: 14px; margin-bottom: 30px;">Поступил Заказ</H4>
	        <p>Номер заказа: {0}</p>
	        <p>Клиент: {4} {5}</p>
	        <p>Номер телефона: {1}</p>
	        <p>Email: {6}</p>
	        <p></p>
	        
			<table style="max-width:600px; width:100%; margin:0; padding:0;" border="0" cellpadding="0">
				<thead>
					<tr>
						<th style="border-bottom: 1px solid #ececec; padding: 14px 0; text-align: left">Товар</th>
						<th style="border-bottom: 1px solid #ececec; padding: 14px 0;">Кол-во</th>
						<th style="border-bottom: 1px solid #ececec; padding: 14px 0;">Сумма</th>
					</tr>
				</thead>
				<tbody>
					{2}
				</tbody>
				<tfoot>
					<tr >
						<td style="border-bottom: 1px solid #ececec; padding: 14px 0;"></td>
						<th style="text-align: center; border-bottom: 1px solid #ececec; padding: 14px 0;">Итого</th>
						<td style="text-align: center; border-bottom: 1px solid #ececec; padding: 14px 0;"><strong><span>&#8381 {3}</span></strong></td>
					</tr>
				</tfoot>
			</table>	

	        <p></p>
			</div>
	      </body>
	    </html>
		""".format(
			order.id,
			order.buyer.phone if order.buyer else '',
			order_items,
			order.total,
			order.buyer.first_name if order.buyer else '',
			order.buyer.last_name if order.buyer else '',
			order.buyer.email if order.buyer else ''
		)


	part1 = MIMEText(text, "plain")
	part2 = MIMEText(html, "html")
	message.attach(part1)
	message.attach(part2)

	context = ssl.create_default_context()

	server = smtplib.SMTP(HOST, 587)
	server.starttls()
	server.login(sender_email, password)
	server.sendmail(sender_email, receiver_email , message.as_string())
	server.quit()	