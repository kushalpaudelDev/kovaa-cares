
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_alter_review_options_alter_review_user'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='review',
            table='reviews',
        ),
    ]
