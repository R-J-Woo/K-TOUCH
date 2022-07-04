from django.shortcuts import render
from django.views.generic import ListView
from .models import Question
# Create your views here.


class QuestionList(ListView):
    model = Question
    template_name = 'question_list.html'
