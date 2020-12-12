from django.shortcuts import render
from django.shortcuts import redirect

from shagr.core import get_context

from .core import exec_registration
from .core import exec_login
from .core import exec_logout
from .core import exec_save


def show_registration_form(request):

	return render(request, 'authapp/registration.html', get_context(request))


def account_reg(request):
	
	if exec_registration(request):
		return render(request, 'authapp/account.html', get_context(request))

	return render(request, 'authapp/error.html', get_context(request))

def account_login(request):

	exec_login(request)
	return redirect(request.META['HTTP_REFERER'])	

def account_logout(request):

	exec_logout(request)
	return redirect(request.META['HTTP_REFERER'])

def account_show(request):

	if request.user.is_authenticated:
		return render(request, 'authapp/account.html', get_context(request))

	return redirect(request.META['HTTP_REFERER'])

def account_save(request):

	if exec_save(request):	
		return render(request, 'authapp/account.html', get_context(request))

	return redirect(request.META['HTTP_REFERER'])