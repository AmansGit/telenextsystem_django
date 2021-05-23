from django.shortcuts import render, redirect

from django.contrib import messages

from .models import Registration
from .forms import RegistrationForm
from django.contrib.auth.hashers import make_password, check_password

import json

# Create your views here.


def signup(request):
	response = {}
	data = []
	if request.method == 'POST':
		
		body = json.loads(request.body)
		username = body['username']
		email = body['email']
		password = body['password']
		
		# form = RegistrationForm(request.POST)
		# if form.is_valid():
		# 	try:
		# 		username = forms.cleaned_data['username']
		# 		email = forms.cleaned_data['email']
		# 		password = forms.cleaned_data['password']
		
		encrypted_pass = make_password(password)

		user_data = Registration(user_name=username, email=email, password=encrypted_pass)
		try:
			user_data.save()
			data = {
				"username": username,
				"email": email
			}
			response = {
				"message": "Successfully registered",
				"data": data
			}
		except:
			response = {
				"message": "Not registered",
				"data": data
			}
	return HttpResponse(json.dumps(response), context='text/json')

def login(request):
	response = {}
	if request.method == 'POST':

		body = json.loads(request.body)
		email = body['email']
		password = body['password']
		
		user_data = Registration.objects.filter(username=username).first()

		if user_data == None:
			response['msg'] = "Data not found"
			response['data'] = None
			response['status'] = "Failed"

		else:
			if check_password(password, user_data.password):
				body = {
					"username": user_data.username,
					"email": user_data.email
				}