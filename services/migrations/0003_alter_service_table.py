
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_alter_service_options_service_created_at'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='service',
            table='services',
        ),
    ]
