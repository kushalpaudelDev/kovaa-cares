
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_alter_payment_options_payment_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='payment',
            table='payments',
        ),
    ]
