# Generated by Django 4.0.5 on 2022-07-03 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_date', models.DateTimeField(verbose_name='예약 날짜')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='예약자 이름')),
            ],
            options={
                'verbose_name': '예약',
                'verbose_name_plural': '예약',
                'db_table': 'reservation',
            },
        ),
    ]
