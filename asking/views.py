from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from asking.models import Question
from django.urls import reverse
# Create your views here.

def ask(request, username):
    user = User.objects.get(username = username)
    template = loader.get_template('asking/asking.html')
    try:
        content_field = request.POST['content']

        user.questions.create(content = content_field, answer = "")
        return HttpResponseRedirect(reverse('asking:asking', args = (username, )))

    except:
        first_name = user.first_name
        last_name = user.last_name
        return HttpResponse(template.render({
            'username': username,
            'first_name': first_name,
            'last_name': last_name,
            }, request))


        
        

   
   
   
    
