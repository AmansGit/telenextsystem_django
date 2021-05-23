from django import forms
from .model import Registration

class RegistrationForm(forms.ModelForm):
	username = forms.CharField(
		label= 'please write ur username',
		required= True
		)
	email = forms.EmailField(max_length=200)
	password = forms.CharField(max_length = 100, widget= forms.PasswordInput)

	class Meta:
		model = Registration
		fields = ['username', 'email', 'password']