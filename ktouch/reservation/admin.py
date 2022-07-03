from django.contrib import admin
from .models import Reservation
# Register your models here.


class ReservAdmin(admin.ModelAdmin):
    list_display = ('user', 'reservation_date')


admin.site.register(Reservation, ReservAdmin)
