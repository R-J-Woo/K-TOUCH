from django import forms
from .models import Question
from user.models import User

CATEGORY_CHOICES = (
    ('시술문의', '시술문의'),
    ('가격문의', '가격문의'),
    ('기타문의', '기타문의')
)


class QuestionForm(forms.Form):
    category = forms.ChoiceField(
        widget=forms.Select(), choices=CATEGORY_CHOICES, label='문의 유형')
    contents = forms.CharField(
        error_messages={
            'required': '질문 내용을 입력해주세요.'
        }, label='질문 내용'
    )
