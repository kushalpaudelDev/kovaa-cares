
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_alter_notification_options_alter_notification_user'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='notification',
            table='notifications',
        ),
    ]
