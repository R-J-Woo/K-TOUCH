from django.db import models

# Create your models here.


class Answer(models.Model):
    question = models.ForeignKey(  # 어떤 질문에 댓글을 달았는지
        'question.Question', on_delete=models.CASCADE, verbose_name='질문')
    user = models.ForeignKey(  # 답변 작성한 사람
        'user.User', on_delete=models.CASCADE, verbose_name='답변자')
    answer = models.TextField(verbose_name='답변')
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return str(self.question)

    class Meta:
        db_table = 'Answer'
        verbose_name = '답변'
        verbose_name_plural = '답변'
