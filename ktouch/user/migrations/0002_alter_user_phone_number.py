# Generated by Django 4.0.5 on 2022-07-03 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(verbose_name='전화 번호'),
        ),
    ]
