from django.urls import reverse
from django.views.generic.edit import CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView as BaseLoginView


class LoginView(BaseLoginView):
    template_name = 'myauth/login.html'

    def get_success_url(self):
        return reverse('asking:profile', args=(self.request.user.username,))


class SignUpView(CreateView):
    template_name = 'myauth/signup.html'
    model = get_user_model()
    fields = ['email', 'first_name', 'last_name', 'username', 'password']

    def get_success_url(self):
        return reverse('myauth:login')

    def form_valid(self, form):
        username_field = self.request.POST['username']
        email_field = self.request.POST['email']
        password_field = self.request.POST['password']
        first_name_field = self.request.POST['first_name']
        last_name_field = self.request.POST['last_name']
        form = User.objects.create_user(
            username_field,
            email_field,
            password_field
        )
        form.first_name = first_name_field
        form.last_name = last_name_field
        form.save()
        return super().form_valid(form)
