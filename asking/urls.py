from django.urls import path
from asking import views

app_name = 'asking'
urlpatterns = [
    path('<str:username>', views.ask, name='asking'),
]