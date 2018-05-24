from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, Http404
from .models import User
from django.contrib.auth import authenticate
# Create your views here.
def index(request):
	template = loader.get_template("login/login.html")
	try:
		username = request.POST['username']
		password = request.POST['password']

		if username == "" or password == "":
				message = "You need to fill username and password"
				return HttpResponse(template.render({'message': message}, request))
		user_list = User.objects.all()

		for u in user_list:
			if username == u.username and password == u.password:
				message = "Successful"
				return HttpResponse(template.render({
					'message': message
				}, request))
			else:
				message = "Fail"
				return HttpResponse(template.render({
					'message': message
				}, request))
	except:
	
		return HttpResponse(template.render({}, request))
	
	