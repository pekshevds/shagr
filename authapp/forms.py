from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class UserForm(forms.Form):

	username  	= forms.CharField(max_length = 191, required=True)
	email  		= forms.CharField(max_length = 191, required=True)
	password  	= forms.CharField(max_length = 40, required=True)
	confirm  	= forms.CharField(max_length = 40, required=True)

class BuyerForm(forms.Form):

	first_name  = forms.CharField(max_length = 150, required=False)
	middle_name = forms.CharField(max_length = 150, required=False)
	last_name  	= forms.CharField(max_length = 150, required=False)
	phone  		= forms.CharField(max_length = 150, required=False)
	address  	= forms.CharField(max_length = 1024, required=False)
	email  		= forms.CharField(max_length = 30, required=False)
	zipcode		= forms.CharField(max_length = 30, required=False)
	locality  	= forms.CharField(max_length = 20, required=False)
	street  	= forms.CharField(max_length = 30, required=False)
	house  		= forms.CharField(max_length = 10, required=False)
	apartments  = forms.CharField(max_length = 10, required=False)
	porch  		= forms.CharField(max_length = 10, required=False)
	floor  		= forms.CharField(max_length = 10, required=False)

class ContactForm(forms.Form):

	contactName 	= forms.CharField(max_length=30, widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Ваше Имя',
			'id': 'form-name',

		}))
	contactPhone 	= forms.CharField(max_length=15, widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Телефон',
			'id': 'form-phone',

		}))
	contactMessage = forms.CharField(max_length=1024, widget=forms.Textarea(attrs={
			'class': 'form-control',
			'placeholder': 'Сообщение',
			'id': 'form-message',
			'rows': '5',
		}))
	captcha 		= ReCaptchaField(widget=ReCaptchaV2Checkbox, required=True)