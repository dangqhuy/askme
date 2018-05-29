from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse
from django.template import loader
from asking.models import Question
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def IndexView(request, username):
    user = User.objects.get(username = username) #user hien dang dang nhap
   
    if request.user == user:
    	check_login = True
    else:
    	check_login = False
    if not check_login :#anonymous
    	# anonymous can ask 
    	try:
    		content_field = request.POST['content_']
    		asker_field = request.POST['asker_'] 
    		user.question_ahihi.create(content = content_field,
    		 name_asker = asker_field,
    		 id_user_receive_id = user.id,
    		 answer ="")
    		return HttpResponseRedirect(reverse('question:index', args = (username, )))
    	except:
    		try:
    			question_list = user.question_ahihi.filter(id_user_receive_id = user.id).all()
    		#loc ra danh sach cac cau hoi theo user
    		except:
    			pass 
    		return render(request, 'question/index.html',
    			{'question_list': question_list,
            	'username': user.username,
            	'first_name': user.first_name,
            	'last_name': user.last_name,
            	'check_login':check_login})
    else: #current user
    	#error = "you have to log in first!"
    	#return render(request, 'authentication/login.html',{"error":error})
    	try:

    		answer_field = request.POST['answer_']
    		question_id = request.POST['question_id']
    		answer_pickup = user.question_ahihi.get(pk = question_id)
    		answer_pickup.answer = answer_field
    		answer_pickup.save()
    		return HttpResponseRedirect(reverse('question:index', args = (username, )))
    	except: 
    		try:
    			question_list = user.question_ahihi.filter(id_user_receive_id = user.id).all()
    		#loc ra danh sach cac cau hoi theo user
    		except:
    			pass 
    		return render(request, 'question/index.html',
    		{'question_list': question_list,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'check_login':check_login})


