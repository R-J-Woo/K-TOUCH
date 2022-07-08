"""ktouch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user.views import home, RegisterView, LoginView, logout, pricing
from question.views import QuestionList, QuestionCreate, QuestionDetail, faq, QuestionUpdate, QuestionDelete
from answer.views import AnswerCreate
from reservation.views import ReservationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', logout),
    path('price/', pricing),
    path('question/', QuestionList.as_view()),
    path('question/create/', QuestionCreate.as_view()),
    path('question/<int:pk>/', QuestionDetail.as_view()),
    path('question/<int:pk>/update/', QuestionUpdate.as_view()),
    path('question/<int:pk>/delete/', QuestionDelete.as_view()),
    path('makereservation/', ReservationView.as_view()),
    path('faq/', faq),
    path('answer/create/', AnswerCreate.as_view()),
]
