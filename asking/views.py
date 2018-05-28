from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from asking.models import Question
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def ask(request, username):
    user = User.objects.get(username = username)
    template = loader.get_template('asking/asking.html')

    check_login = True
    if request.user == user:
        check_login = True
    else:
        check_login = False
    if not check_login:
        try:
   
            content_field = request.POST['content']
            if content_field is not None:
                user.questions.create(content = content_field, answer = "")
        
            return HttpResponseRedirect(reverse('asking:asking', args = (username, )))

        except:
            try:
                question = user.questions.filter(answerer_id = user.id).all()
            except:
                pass

            first_name = user.first_name
            last_name = user.last_name

            return HttpResponse(template.render({
                'question': question,
                'username': username,
                'first_name': first_name,
                'last_name': last_name,
                'check_login': check_login,
                }, request))
    else:
        try:
            question_id = request.POST['question_id']
            answer_field = request.POST['answer']
            answer = user.questions.get(pk = question_id)
            answer.answer = answer_field
            answer.save()
            return HttpResponseRedirect(reverse('asking:asking', args = (username, )))

        except:
            try:
                question = user.questions.filter(answerer_id = user.id).all()
            except:
                pass

            first_name = user.first_name
            last_name = user.last_name

            return HttpResponse(template.render({
                'question': question,
                'username': username,
                'first_name': first_name,
                'last_name': last_name,
                'check_login': check_login,
                }, request))


        
        

   
   
   
    
