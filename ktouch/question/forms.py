from django import forms
from .models import Question
from user.models import User


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['category', 'contents']
