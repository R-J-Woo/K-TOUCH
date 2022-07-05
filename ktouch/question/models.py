from tkinter import CASCADE
from django.db import models

# Create your models here.
CATEGORY_CHOICES = {
    ('시술문의', '시술문의'),
    ('가격문의', '가격문의'),
    ('기타문의', '기타문의')
}


class Question(models.Model):
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, verbose_name='질문자 이름')
    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        verbose_name='문의 유형'
    )
    contents = models.TextField(verbose_name='질문 내용')
    register_date = models.DateTimeField(
        verbose_name='질문 날짜', auto_now_add=True)

    def __str__(self):
        return self.contents

    class Meta:
        db_table = 'question'
        verbose_name = '질문'
        verbose_name_plural = '질문'
