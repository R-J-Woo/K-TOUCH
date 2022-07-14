from distutils.log import Log
from django.shortcuts import render, redirect
from django.views.generic import FormView, ListView
from django.utils.decorators import method_decorator
from .forms import RegisterForm, LoginForm
from question.models import Question
from reservation.models import Reservation
from .models import User
from .decorators import login_required
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


@method_decorator(login_required, name='dispatch')
class MyPage(ListView):
    template_name = 'myhistory.html'
    paginate_by = 2
    page_kwarg = 'page'

    def get_queryset(self, **kwargs):
        queryset = Question.objects.filter(
            user__uid=self.request.session.get('uid'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservations'] = Reservation.objects.filter(
            user__uid=self.request.session.get('uid'))
        return context
