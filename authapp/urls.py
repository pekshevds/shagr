from django.urls import path
from django.urls import include

from .views import show_registration_form
from .views import account_reg
from .views import account_login
from .views import account_logout
from .views import account_show
from .views import account_save

urlpatterns = [
	
	# visual
	path('registration/', 	show_registration_form, name='show_registration_form'),
	path('account/', 		account_show, name='account_show'),	
	# executable
	path('account_reg/', 	account_reg, name='account_reg'),
	path('account_save/', 	account_save, name='account_save'),
	path('account_login/', 	account_login, name='account_login'),
	path('account_logout/', account_logout, name='account_logout'),
]