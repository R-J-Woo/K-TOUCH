from django.db import models

# Create your models here.


class Question(models.Model):
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, verbose_name='질문자 이름')
    contents = models.TextField(verbose_name='질문 내용')
    register_date = models.DateTimeField(verbose_name='질문 날짜')

    def __str__(self):
        return self.contents

    class Meta:
        db_table = 'question'
        verbose_name = '질문'
        verbose_name_plural = '질문'
