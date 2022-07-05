from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .models import Question
from .forms import QuestionForm
from user.models import User
# Create your views here.


class QuestionList(ListView):
    model = Question
    paginate_by = 15
    page_kwarg = 'page'
    ordering = '-register_date'
    template_name = 'question_list.html'


class QuestionCreate(FormView):
    template_name = 'question_register.html'
    form_class = QuestionForm
    success_url = '/question/'

    def form_valid(self, form):
        question = Question(
            user=User.objects.get(uid=self.request.session['uid']),
            category=form.data.get('category'),
            contents=form.data.get('contents')
        )
        question.save()

        return super().form_valid(form)
