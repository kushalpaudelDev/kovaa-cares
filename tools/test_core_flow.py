import os
import django
import sys
from datetime import datetime, timedelta

# Setup Django environment
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()

from django.contrib.auth import get_user_model
from pets.models import Pet
from services.models import Service
from appointments.models import Appointment
from payments.models import Payment
from notifications.models import Notification

User = get_user_model()

print('Starting core flow test')

# 1. Create or get user
username = 'testuser_copilot'
password = 'testpass123'
user, created = User.objects.get_or_create(username=username)
if created:
    user.set_password(password)
    user.save()
    print('Created user', user.username)
else:
    print('User exists', user.username)

# 2. Create pet linked to user
pet, created = Pet.objects.get_or_create(
    owner=user,
    name='Rex',
    defaults={'species': 'Dog', 'age': 2, 'gender': 'Male', 'breed': ''}
)
print('Pet:', pet, 'created=', created)

# 3. Create service
service, created = Service.objects.get_or_create(name='Basic Checkup', defaults={'description': 'Checkup', 'price': 20.00, 'duration': 30})
print('Service:', service, 'created=', created)

# 4. Create appointment
appt_dt = datetime.now() + timedelta(days=2)
appointment = Appointment.objects.create(pet=pet, service=service, appointment_date=appt_dt)
print('Appointment created:', appointment, 'status=', appointment.status)

# 5. Create payment (mark as Paid to trigger signal)
payment = Payment.objects.create(appointment=appointment, amount=service.price, payment_method='card', transaction_id='tx12345', status='Paid')
print('Payment created:', payment, 'status=', payment.status)

# 6. Check notification auto-create
notifs = Notification.objects.filter(user=user).order_by('-created_at')
print('Notifications for user:', notifs.count())
for n in notifs[:5]:
    print('-', n.title, ':', n.message)

print('Done')
