from django.shortcuts import render
from django.views.generic import FormView
from .forms import ReservationForm
from .models import Reservation
from user.models import User

# Create your views here.


class ReserveView(FormView):  # 예약하는 view
    template_name = 'make_reservation.html'
    form_class = ReservationForm
    success_url = '/'

    def form_valid(self, form):
        reservation = Reservation(
            user=User.objects.get(uid=self.request.session['uid']),
            service=form.data.get('service'),
            reservation_date=form.data.get('reservation_date')
        )
        reservation.save()

        return super().form_valid(form)
