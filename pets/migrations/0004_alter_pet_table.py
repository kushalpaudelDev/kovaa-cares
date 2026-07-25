
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_alter_pet_options_alter_pet_owner'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='pet',
            table='pets',
        ),
    ]
