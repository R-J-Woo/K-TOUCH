from django.contrib import admin
from .models import Answer
# Register your models here.


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')


admin.site.register(Answer, AnswerAdmin)
