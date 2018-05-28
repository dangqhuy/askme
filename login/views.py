from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.urls import reverse


def login(request):
	template = loader.get_template("login/login.html")
	try:
		username_field = request.POST['username']
		password_field = request.POST['password']
		
		user_auth = authenticate(username = username_field, password = password_field)

		if (user_auth is not None) and (not user_auth.is_superuser):
			auth_login(request, user_auth)
			return HttpResponseRedirect(reverse('asking:asking', args = (user_auth.username, )))
			
		else:
			message = "Log in fail (Wrong username or password)"
			return  HttpResponse(template.render({
				'message': message
			}, request))

	except:
		return HttpResponse(template.render({}, request))
		
def signup(request):
	
	template_signup = loader.get_template('login/signup.html')
	template_login = loader.get_template('login/login.html')
	message = "Sign up success"
	try:
		email_field = request.POST['email']
		firstname_field = request.POST['firstname']
		lastaname_field= request.POST['lastname']
		username_field = request.POST['username']
		password_field = request.POST['password']

		user = User.objects.create_user(username_field, email_field, password_field)
		user.first_name = firstname_field
		user.last_name = lastaname_field
		user.save()
		return HttpResponse(template_login.render({
			'message': message
		}, request))

	except:
		return HttpResponse(template_signup.render({}, request))
	
	


	
	


	
	