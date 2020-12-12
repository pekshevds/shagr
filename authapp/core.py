from django.contrib.auth.models import User
from .models import Buyer

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

from .forms import UserForm
from .forms import BuyerForm

def exec_registration(request):
	
	if request.method == 'POST':
		
		userForm = UserForm(request.POST)
		if userForm.is_valid():
			
			username = userForm.cleaned_data['username']
			email = userForm.cleaned_data['email']
			password = userForm.cleaned_data['password']
			confirm = userForm.cleaned_data['confirm']

			if password != confirm:				
				return False


			try:
				user = User.objects.get(username=username, email=email)
			except:
				user = None

			if not user:
				user = User.objects.create_user(username=username, email=email, password=password, is_staff=False, is_active=True)

				exec_logout(request)
				login(request, user)

				return True
	return False


def exec_logout(request):

	if request.user.is_authenticated:
		logout(request)


def exec_login(request):

	if request.method == 'POST':

		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)


def exec_save(request):

	if request.user.is_authenticated and request.method == 'POST':
		
		buyerForm = BuyerForm(request.POST)
		if buyerForm.is_valid():

			
			try:
				buyer = Buyer.objects.get(user=request.user)
			except:
				buyer = Buyer.objects.create(user=request.user)

			buyer.first_name  	= buyerForm.cleaned_data['first_name']
			buyer.last_name  	= buyerForm.cleaned_data['last_name']
			buyer.phone  		= buyerForm.cleaned_data['phone']
			buyer.address  		= buyerForm.cleaned_data['address']
			buyer.email  		= buyerForm.cleaned_data['email']
			buyer.locality  	= buyerForm.cleaned_data['locality']
			buyer.street  		= buyerForm.cleaned_data['street']
			buyer.house  		= buyerForm.cleaned_data['house']
			buyer.apartments  	= buyerForm.cleaned_data['apartments']
			buyer.porch  		= buyerForm.cleaned_data['porch']
			buyer.floor  		= buyerForm.cleaned_data['floor']

			try:
				buyer.save()
			except:
				return False

			return True
	return False
