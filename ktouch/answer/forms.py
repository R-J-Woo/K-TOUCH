from distutils.log import error
from django import forms
from .models import Answer
from user.models import User
from question.models import Question


class RegisterForm(forms.Form):
    # 작성자의 경우에는 입력하는 값이 아닌, 로그인한 정보가 자동으로 전달되어야 한다
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    # post는 post의 id로 받을 것이기 때문에 IntegerField를 사용한다
    question = forms.IntegerField(
        widget=forms.HiddenInput
    )
    answer = forms.CharField(
        error_messages={
            'required': '답변을 입력해주세요.'
        }, label='답변 작성하기'
    )

    def clean(self):
        cleaned_data = super().clean()
        question = cleaned_data.get('question')
        answer = cleaned_data.get('answer')
        uid = self.request.session.get('uid')

        if question and answer and uid:
            answer = Answer(
                question=Question.objects.get(pk=question),
                answer=answer,
                user=User.objects.get(uid=uid)
            )
            answer.save()
        else:
            self.question = question
            self.add_error('answer', '답변이 입력되지 않았습니다.')
