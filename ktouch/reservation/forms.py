from django import forms
from .models import Reservation
from user.models import User

SERVICE_CHOICES = (
    ('헤어 라인', '헤어 라인'),
    ('입술 반영구', '입술 반영구'),
    ('눈썹 반영구', '눈썹 반영구'),
    ('아이라인', '아이라인')
)


class ReservationForm(forms.Form):
    service = forms.ChoiceField(
        widget=forms.Select(), choices=SERVICE_CHOICES, label='예약 서비스')
    reservation_date = forms.DateTimeField()
