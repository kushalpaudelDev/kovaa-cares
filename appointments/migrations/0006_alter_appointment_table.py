
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0005_alter_appointment_options_alter_appointment_pet_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='appointment',
            table='appointments',
        ),
    ]
