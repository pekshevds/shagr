from django.shortcuts import render
from django.shortcuts import redirect

from django.urls import reverse, reverse_lazy

from shagr.core import get_context

from .core import exec_registration
from .core import exec_login
from .core import exec_logout
from .core import exec_save

from allauth.account.utils import passthrough_next_redirect_url, get_request_param
from django.contrib.sites.shortcuts import get_current_site
from allauth.account.views import LoginView, SignupView, LogoutView


def show_registration_form(request):
	if request.user.is_authenticated:
		return render(request, 'authapp/account.html', get_context(request))
	else:
		return render(request, 'authapp/registration.html', get_context(request))


def account_reg(request):
	
	if exec_registration(request):
		return render(request, 'authapp/account.html', get_context(request))

	return render(request, 'authapp/error.html', get_context(request))

def account_login(request):

	exec_login(request)
	if request.user.is_authenticated:
		return render(request, 'authapp/account.html', get_context(request))
	return redirect(request.META['HTTP_REFERER'])	

def account_logout(request):

	exec_logout(request)
	return redirect('show_index')

def account_show(request):

	if request.user.is_authenticated:
		return render(request, 'authapp/account.html', get_context(request))

	return redirect(request.META['HTTP_REFERER'])

def account_save(request):

	if exec_save(request):
		return redirect(request.META['HTTP_REFERER'])
		
	return redirect(request.META['HTTP_REFERER'])


class CustomSignupView(SignupView):

	def get_context_data(self, **kwargs):

		ret = super(SignupView, self).get_context_data(**kwargs)

		form = ret['form']
		email = self.request.session.get('account_verified_email')

		if email:
			email_keys = ['email']
			if app_settings.SIGNUP_EMAIL_ENTER_TWICE:
				email_keys.append('email2')
			for email_key in email_keys:
				form.fields[email_key].initial = email

		login_url = passthrough_next_redirect_url(self.request,reverse("account_login"),self.redirect_field_name)
		redirect_field_name = self.redirect_field_name
		redirect_field_value = get_request_param(self.request,redirect_field_name)

		ret.update({'login_url': login_url,
	                'redirect_field_name': redirect_field_name,
	                'redirect_field_value': redirect_field_value,
	                })

		ret.update(get_context(self.request))

		return ret

class CustomLoginView(LoginView):

	def get_context_data(self, **kwargs):

		ret = super(LoginView, self).get_context_data(**kwargs)
		signup_url = passthrough_next_redirect_url(self.request,reverse('account_signup'),self.redirect_field_name)

		redirect_field_value = get_request_param(self.request,self.redirect_field_name)
		site = get_current_site(self.request)

		ret.update({'signup_url': signup_url,
                    'site': site,
                    'redirect_field_name': self.redirect_field_name,
                    'redirect_field_value': redirect_field_value,
        			})

		ret.update(get_context(self.request))

		return ret

class CustomLogoutView(LogoutView):

	def get_context_data(self, **kwargs):

		ret = {}
		# ret = super(LogoutView, self).get_context_data(**kwargs)
		logout_url = passthrough_next_redirect_url(self.request,reverse('account_logout'),self.redirect_field_name)

		redirect_field_value = get_request_param(self.request,self.redirect_field_name)
		site = get_current_site(self.request)

		ret.update({'logout_url': logout_url,
                    'site': site,
                    'redirect_field_name': self.redirect_field_name,
                    'redirect_field_value': redirect_field_value,
        			})

		ret.update(get_context(self.request))

		return ret	
