import myauth.views as myauth_views
from django.urls import path


app_name = 'myauth'
urlpatterns = [
    path('login/', myauth_views.LoginView.as_view(), name='login'),
    path('signup/', myauth_views.SignUpView.as_view(), name="signup"),

]
