# Generated by Django 5.0 on 2024-05-27 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hestia', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['last_name', 'username'], 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='username',
        ),
    ]
