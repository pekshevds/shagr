from django.urls import path
from django.urls import include
from .views import show_profile
from .views import CustomPasswordChangeView, account_password_change_succes, CustomLoginView
from .views import CustomSignupView, CustomPasswordResetView, CustomPasswordResetDoneView
from .views import CustomPasswordResetFromKeyView, profile_change, profile_add

urlpatterns = [

	
	path('profile/change/<str:buyer_id>/', profile_change, name='profile_change'),
	
	path('profile/add/', profile_add, name='profile_add'),

	path('profile/', show_profile, name='show_profile'),

	path('login/', CustomLoginView.as_view(), name='account_login'),

	path('signup/', CustomSignupView.as_view(), name='account_signup'),
	
	path('password/reset/key/', CustomPasswordResetFromKeyView.as_view(), name='account_reset_password_from_key'),
	
	path('password/reset/done/', CustomPasswordResetDoneView.as_view(), name='account_reset_password_done'),

	path('password/reset/', CustomPasswordResetView.as_view(), name='account_reset_password'),

	path('password/change/success/', account_password_change_succes, name='account_password_change_succes'),

	path('password/change/', CustomPasswordChangeView.as_view(), name='account_password_change'),

	path(''		 		, include('allauth.urls')),

]
