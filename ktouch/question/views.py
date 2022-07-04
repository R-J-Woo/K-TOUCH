from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .models import Question
from .forms import QuestionForm
# Create your views here.


class QuestionList(ListView):
    model = Question
    template_name = 'question_list.html'


class QuestionCreate(FormView):
    template_name = 'question_register.html'
    form_class = QuestionForm
    success_url = '/question/'
