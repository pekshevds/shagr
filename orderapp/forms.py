from django import forms


class OrderForm(forms.Form):

	first_name  = forms.CharField(max_length = 150)
	last_name  	= forms.CharField(max_length = 150)
	company_name  = forms.CharField(max_length = 150, required=False)
	company_inn  = forms.CharField(max_length = 20, required=False)
	zipcode		= forms.CharField(max_length = 30, required=False)
	locality  	= forms.CharField(max_length = 20, required=False)
	street  	= forms.CharField(max_length = 30, required=False)
	house  		= forms.CharField(max_length = 30, required=False)
	apartments  = forms.CharField(max_length = 30, required=False)
	porch  		= forms.CharField(max_length = 10, required=False)
	floor  		= forms.CharField(max_length = 10, required=False)
	email  		= forms.CharField(max_length = 30, required=False)
	phone  		= forms.CharField(max_length = 150, required=False)
	checkout_payment_method = forms.CharField(max_length = 2)
	checkout_delivery_type = forms.CharField(max_length = 2)
	checkout_terms = forms.BooleanField(required=False)



	middle_name = forms.CharField(max_length = 150, required=False)
	address  	= forms.CharField(max_length = 1024, required=False)
	
	
	
	
	
	
	
	