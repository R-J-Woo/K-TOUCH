from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import RegisterForm
# Create your views here.


class AnswerCreate(FormView):  # 댓글 생성하는 view
    form_class = RegisterForm
    success_url = '/question/'

    def form_invalid(self, form):  # 댓글 작성에 실패했을 경우에 실행
        return redirect('/question/' + str(form.question))

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw
