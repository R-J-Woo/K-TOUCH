# Generated by Django 4.0.5 on 2022-07-15 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_alter_reservation_reservation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='service',
            field=models.CharField(choices=[('헤어 라인', '헤어 라인'), ('입술 반영구', '입술 반영구'), ('눈썹 반영구', '눈썹 반영구'), ('아이라인', '아이라인')], max_length=10, verbose_name='예약 서비스'),
        ),
    ]
