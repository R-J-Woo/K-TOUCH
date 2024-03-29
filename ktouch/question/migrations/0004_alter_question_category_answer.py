# Generated by Django 4.0.5 on 2022-07-05 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_phone_number'),
        ('question', '0003_question_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(choices=[('기타문의', '기타문의'), ('가격문의', '가격문의'), ('시술문의', '시술문의')], max_length=10, verbose_name='문의 유형'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(verbose_name='답글')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.question', verbose_name='질문')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='질문자')),
            ],
            options={
                'verbose_name': '답글',
                'verbose_name_plural': '답글',
                'db_table': 'Answer',
            },
        ),
    ]
