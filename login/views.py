from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login as user_ahihi
from django.contrib.auth.models import User
from django.urls import reverse


def login1(request): 
	template = loader.get_template("authentication/login.html")
	try:	
		username_field = request.POST['username']
		password_field = request.POST['password']

		user_auth = authenticate(username = username_field, password = password_field)
		
		if user_auth is not None and not user_auth.is_superuser:
			user_ahihi(request,user_auth) #DONG CODE THAN THANH!!!
			error = "successful!!"
			username = User.objects.get(username = username_field).username
			#return HttpResponse("work")
			
			return HttpResponseRedirect(reverse('question:index', args = (username, )))
			#return render(request, 'authentication/layout_1.html',{"error":error, "info":info})
			
		else:
			error = "Your information is not right!"
			return render(request, 'authentication/login.html',{"error":error})

		
	except:
		return HttpResponse(template.render({}, request))
def signup1(request):
	template_signup = loader.get_template('authentication/signup.html')
	template_login = loader.get_template('authentication/login.html')
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
		message = "successful register, now, Plz sign in :3"
		#return HttpResponseRedirect(reverse('question:index', args = (username, )))
		return HttpResponse(template_login.render({'message': message}, request))
	except:
		return HttpResponse(template_signup.render({}, request))
	

	
