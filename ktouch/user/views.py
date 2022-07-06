from distutils.log import Log
from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import RegisterForm, LoginForm
# Create your views here.


def home(request):  # 메인 페이지
    return render(request, 'home.html', {'uid': request.session.get('uid')})


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):  # 유효성 검사가 끝나고 세션 처리를 해주기 위함
        self.request.session['uid'] = form.uid
        return super().form_valid(form)


def logout(request):
    if 'uid' in request.session:
        del(request.session['uid'])

    return redirect('/')


def pricing(request):  # 가격
    return render(request, 'pricing.html')
