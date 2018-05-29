from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from asking.models import Question
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout as auth_logout


def ask(request, username):
    user = User.objects.get(username=username)
    template = loader.get_template('asking/asking.html')

    check_login = True
    if request.user == user:
        check_login = True
    else:
        check_login = False

    if not check_login:
        try:
            content_field = request.POST['content']
            user.questions.create(content=content_field, answer="")
            return HttpResponseRedirect(reverse('asking:asking', args=(username,)))

        except BaseException:
            try:
                question = user.questions.filter(answerer_id=user.id).all()
            except BaseException:
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
            try:
                if request.POST['check_logout'] == "logout":
                    auth_logout(request)
                    return HttpResponseRedirect(reverse("login:login"))
            except:

                question_id = request.POST['question_id']
                answer_field = request.POST['answer']
                answer = user.questions.get(pk=question_id)
                answer.answer = answer_field
                answer.save()
            

                return HttpResponseRedirect(
                    reverse('asking:asking', args=(username, )))

        except BaseException:
            try:
                question = user.questions.filter(answerer_id=user.id).all()
            except BaseException:
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

