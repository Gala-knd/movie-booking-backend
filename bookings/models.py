from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from users.models import User
from shows.models import Session
from halls.models import Seat
import qrcode
from io import BytesIO
from django.core.files import File

class Booking(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    booking_code = models.CharField(max_length=50, unique=True)
    is_paid = models.BooleanField(default=False)
    booked_at = models.DateTimeField(auto_now_add=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    class Meta:
        unique_together = ('session', 'seat')

    def clean(self):
        if self.session.start_time < timezone.now():
            raise ValidationError('Нельзя бронировать билеты на прошедший сеанс')
        if not self.session.hall.is_active:
            raise ValidationError('Продажа билетов на этот сеанс временно закрыта')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.session} - {self.seat}"

    def generate_qr(self):
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(f'Booking: {self.booking_code}')
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        blob = BytesIO()
        img.save(blob, 'PNG')
        self.qr_code.save(f'{self.booking_code}.png', File(blob), save=True)
