from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.
def login(request):
	template = loader.get_template("login/login.html")
	try:
		username_field = request.POST['username']
		password_field = request.POST['password']

		user_auth = authenticate(username = username_field, password = password_field)
		if user_auth is not None:
			return HttpResponse("success")
		else:
			return  HttpResponse("fail")
	except:
		return HttpResponse(template.render({}, request))
		
	


	
	