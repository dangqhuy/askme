from django.urls import path
import asking.views as ask_views


app_name = 'asking'
urlpatterns = [
    path(
        'profile/<str:slug>',
        ask_views.ProfileView.as_view(),
        name="profile"
    ),
    path(
        'asking/<str:slug>',
        ask_views.AskView.as_view(),
        name='asking'
    ),
    path(
        'question/<int:pk>',
        ask_views.UpdateQuestionView.as_view(),
        name="question"
    )
]
