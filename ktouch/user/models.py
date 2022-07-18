from django.db import models

# Create your models here.


class User(models.Model):
    uid = models.CharField(verbose_name='아이디', max_length=16, unique=True)
    password = models.CharField(verbose_name='비밀번호', max_length=200)
    phone_number = models.CharField(verbose_name='전화 번호', max_length=16)
    name = models.CharField(verbose_name='이름', max_length=16)
    register_date = models.DateTimeField(
        verbose_name='가입 날짜', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
