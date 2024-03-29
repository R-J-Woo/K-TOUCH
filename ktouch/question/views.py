from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from .models import Question
from .forms import QuestionForm
from answer.forms import RegisterForm as AnswerForm
from answer.models import Answer
from user.models import User
from django.utils.decorators import method_decorator
from user.decorators import login_required
# Create your views here.


class QuestionList(ListView):
    model = Question
    paginate_by = 15
    page_kwarg = 'page'
    ordering = '-register_date'
    template_name = 'question_list.html'


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
class QuestionDetail(DetailView):
    template_name = 'question_detail.html'
    queryset = Question.objects.all()
    context_object_name = 'question'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AnswerForm(self.request)
        context['answers'] = Answer.objects.filter(question=self.kwargs['pk'])
        return context


def faq(request):
    return render(request, 'faq.html')


@method_decorator(login_required, name='dispatch')
class QuestionUpdate(UpdateView):
    model = Question
    form_class = QuestionForm
    success_url = '/question/'
    template_name = 'question_update.html'


@method_decorator(login_required, name='dispatch')
class QuestionDelete(DeleteView):
    model = Question
    success_url = '/question/'
    template_name = 'question_confirm_delete.html'
