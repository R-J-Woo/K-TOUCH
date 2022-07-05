# Generated by Django 4.0.5 on 2022-07-05 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0007_alter_question_category_delete_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(choices=[('기타문의', '기타문의'), ('시술문의', '시술문의'), ('가격문의', '가격문의')], max_length=10, verbose_name='문의 유형'),
        ),
    ]