# Generated by Django 5.0.6 on 2024-06-03 17:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hestia', '0016_property_image_01_property_image_02_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hestia.property')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hestia.client')),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Carts',
            },
        ),
        migrations.DeleteModel(
            name='PropertyImage',
        ),
    ]
