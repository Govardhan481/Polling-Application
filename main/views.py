from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    DetailView,
    ListView,
    FormView,
    TemplateView
    )
from main import models,forms
from django.views.generic.detail import SingleObjectMixin,BaseDetailView
from django.contrib.auth.mixins import PermissionRequiredMixin


# Create your views here.
class Index(ListView):
    model = models.Question
    template_name='main/index.html'

#@login_required
class Question(PermissionRequiredMixin, SingleObjectMixin, FormView):
  model = models.Question
  template_name = 'main/question.html'
  form_class = forms.AnswerForm
  permission_required ='add_answer'


  def form_valid(self, form):
    obj = form.save(commit = False)
    obj.question = self.get_object()
    obj.user = self.request.user
    obj.save()
    return HttpResponseRedirect('/')

  def get_context_data(self, **kwargs):
    data = super().get_context_data(**kwargs)
    try:
      data['answer']= models.Answer.objects.get(question = self.get_object(),user = self.request.user)
    except models.Answer.DoesNotExist:
      data['answer']=None
    return data

  def post(self, request, *args, **kwargs):
    self.object = self.get_object()
    return super().post(request, *args, **kwargs)

  def get(self, request, *args, **kwargs):
    self.object = self.get_object()
    context = self.get_context_data(object=self.object)
    return self.render_to_response(context)



class dash_questions(ListView):
    model = models.Question
    template_name='main/dash_questions.html'


class dash_question(DetailView):
  model = models.Question
  template_name = 'main/dash_question.html'

  def get_context_data(self, **kwargs):
    data = super().get_context_data(**kwargs)
    try:
      data['answer']= models.Answer.objects.get(question = self.get_object(),user = self.request.user)
    except models.Answer.DoesNotExist:
      data['answer']=None
    return data

  

  
