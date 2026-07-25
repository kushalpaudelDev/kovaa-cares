
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0004_alter_appointment_service'),
        ('pets', '0003_alter_pet_options_alter_pet_owner'),
        ('services', '0002_alter_service_options_service_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'ordering': ['-appointment_date', '-created_at'], 'verbose_name_plural': 'Appointments'},
        ),
        migrations.AlterField(
            model_name='appointment',
            name='pet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='pets.pet'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='services.service'),
        ),
    ]
