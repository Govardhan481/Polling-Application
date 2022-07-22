from django.urls import path
from main import views
from django.contrib.auth.decorators import login_required

urlpatterns=[
    path('',views.Index.as_view(),name='index'),
    path('question/<slug>',login_required(views.Question.as_view()),name='question'),
    path('dash_questions',login_required(views.dash_questions.as_view()),name='dashboard'),
    path('dash_question/<slug>',login_required(views.dash_question.as_view()),name='dash_question'),
]