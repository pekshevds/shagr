from django.urls import path
from django.urls import include

from .views import show_registration_form
from .views import account_reg
from .views import account_login
from .views import account_logout
from .views import account_show
from .views import account_save

from .views import CustomSignupView, CustomLoginView, CustomLogoutView

urlpatterns = [
	
	# visual
	path('auth/', 	show_registration_form, name='show_registration_form'),
	path('profile/', 		account_show, name='account_show'),	
	# executable
	path('account_reg/', 	account_reg, name='account_reg'),
	path('account_save/', 	account_save, name='account_save'),
	
	path('signup/', CustomSignupView.as_view(), name='account_signup'),
	path('login/', CustomLoginView.as_view(), name='account_login'),
	path('logout/', CustomLogoutView.as_view(), name='account_logout'),
	path(''		 		, include('allauth.urls')),

]