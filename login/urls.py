from django.urls import path
from login import views
from django.contrib.auth.views import logout


app_name = "authentication" #registed namespace
urlpatterns = [
	path('', views.login1 , name = 'login'),
	path('signup/', views.signup1, name = 'signup'),
	#path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout')
	path('logout/', logout, {'next_page': 'authentication:login'}, name='logout')
]
