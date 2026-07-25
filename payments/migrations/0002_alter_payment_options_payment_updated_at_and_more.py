
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0005_alter_appointment_options_alter_appointment_pet_and_more'),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'ordering': ['-paid_at'], 'verbose_name_plural': 'Payments'},
        ),
        migrations.AddField(
            model_name='payment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='appointment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='appointments.appointment'),
        ),
    ]
