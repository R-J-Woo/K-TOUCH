from django.db import models

# Create your models here.


class Reservation(models.Model):
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, verbose_name='예약자 이름')
    reservation_date = models.DateTimeField(verbose_name='예약 날짜')

    def __str__(self):
        return str(self.user)

    class Meta:
        db_table = 'reservation'
        verbose_name = '예약'
        verbose_name_plural = '예약'
