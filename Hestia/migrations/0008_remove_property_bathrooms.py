# Generated by Django 5.0 on 2024-05-29 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hestia', '0007_remove_property_prop_type_property_apartment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='bathrooms',
        ),
    ]
