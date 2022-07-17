from msilib.schema import ServiceInstall
from django.db import models
from django.core.exceptions import ValidationError
import datetime

# Create your models here.
SERVICE_CHOICES = {
    ('헤어 라인', '헤어 라인'),
    ('입술 반영구', '입술 반영구'),
    ('눈썹 반영구', '눈썹 반영구'),
    ('아이라인', '아이라인')
}


class Reservation(models.Model):
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, verbose_name='예약자 이름')
    service = models.CharField(
        max_length=10, choices=SERVICE_CHOICES, verbose_name='예약 서비스')
    reservation_date = models.DateField(verbose_name='예약 날짜')

    def __str__(self):
        return str(self.user) + str(self.service)

    class Meta:
        db_table = 'reservation'
        verbose_name = '예약'
        verbose_name_plural = '예약'
