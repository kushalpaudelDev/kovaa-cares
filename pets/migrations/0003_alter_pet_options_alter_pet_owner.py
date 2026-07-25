
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_rename_type_pet_species_pet_age_pet_breed_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pet',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'Pets'},
        ),
        migrations.AlterField(
            model_name='pet',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pets', to=settings.AUTH_USER_MODEL),
        ),
    ]
