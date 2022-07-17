# Generated by Django 4.0.5 on 2022-07-15 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_reservation_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='reservation_date',
            field=models.DateField(verbose_name='예약 날짜'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='service',
            field=models.CharField(choices=[('아이라인', '아이라인'), ('입술 반영구', '입술 반영구'), ('헤어 라인', '헤어 라인'), ('눈썹 반영구', '눈썹 반영구')], max_length=10, verbose_name='예약 서비스'),
        ),
    ]