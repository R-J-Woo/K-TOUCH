# Generated by Django 4.0.5 on 2022-07-18 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0008_alter_reservation_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='service',
            field=models.CharField(choices=[('눈썹 반영구', '눈썹 반영구'), ('헤어 라인', '헤어 라인'), ('아이라인', '아이라인'), ('입술 반영구', '입술 반영구')], max_length=10, verbose_name='예약 서비스'),
        ),
    ]
