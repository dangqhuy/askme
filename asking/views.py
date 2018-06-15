from django.views.generic import CreateView, ListView, UpdateView
from asking.models import Question
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User


class AskView(CreateView):
    template_name = "asking/asking.html"
    model = Question
    fields = ["content"]
    slug_field = 'username'

    def get_success_url(self):
        user = User.objects.get(username=self.request.path.split('/')[-1])
        messages.add_message(
            self.request,
            messages.INFO,
            'Sent question is success'
        )
        return reverse('asking:asking', args=(user.username,))

    def form_valid(self, form):
        user = User.objects.get(username=self.request.path.split('/')[-1])
        form.instance.content = self.request.POST['content']
        form.instance.answerer_id = user.id
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        user = User.objects.get(username=self.request.path.split('/')[-1])
        context = super().get_context_data(**kwargs)
        context['first_name'] = user.first_name
        context['last_name'] = user.last_name
        context['username'] = user.username
        return context


class ProfileView(ListView):
    template_name = 'asking/profile.html'
    model = Question
    fields = ['answer']
    slug_field = "username"

    def get_queryset(self):
        return self.request.user.questions.all()

    def get_success_url(self):
        return reverse('asking:profile', args=(self.request.user.username,))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first_name'] = self.request.user.first_name
        context['last_name'] = self.request.user.last_name
        context['username'] = self.request.user.username
        return context


class UpdateQuestionView(UpdateView):
    model = Question
    fields = ['answer']

    def get_success_url(self):
        return reverse_lazy(
            'asking:profile',
            args=(self.request.user.username,)
        )
