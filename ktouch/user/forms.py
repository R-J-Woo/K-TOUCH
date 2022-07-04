from django import forms
from .models import User
from django.db import IntegrityError
from django.contrib.auth.hashers import check_password, make_password


class RegisterForm(forms.Form):
    uid = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요.'
        }, max_length=64, label='아이디'
    )
    name = forms.CharField(
        error_messages={
            'required': '이름을 입력해주세요.'
        }, max_length=64, label='이름'
    )
    phone_number = forms.IntegerField(
        error_messages={
            'required': '전화번호를 입력해주세요.'
        }, label='전화번호'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )
    re_password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호 확인'
    )

    def clean(self):
        cleaned_data = super().clean()
        uid = cleaned_data.get('uid')
        name = cleaned_data.get('name')
        phone_number = cleaned_data.get('phone_number')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if uid and name and phone_number and password and re_password:
            if password != re_password:
                self.add_error('password', '비밀번호가 서로 다릅니다.')
                self.add_error('re_password', '비밀번호가 서로 다릅니다.')
            else:
                try:  # user id가 이미 존재하고 있을 때 error처리
                    user = User(
                        uid=uid,
                        name=name,
                        phone_number=phone_number,
                        password=make_password(password)
                    )
                    user.save()
                except IntegrityError:
                    self.add_error('uid', '아이디가 이미 존재합니다.')


class LoginForm(forms.Form):
    uid = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요.'
        }, max_length=64, label='아이디'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )

    def clean(self):
        cleaned_data = super().clean()
        uid = cleaned_data.get('uid')
        password = cleaned_data.get('password')

        if uid and password:
            try:
                user = User.objects.get(uid=uid)
            except User.DoesNotExist:
                self.add_error('uid', '아이디가 없습니다.')
                return

            if not check_password(password, user.password):  # password가 일치하지 않으면
                self.add_error('password', '비밀번호를 틀렸습니다.')
            else:
                self.uid = user.uid
