# Generated by Django 4.2.6 on 2023-11-01 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_code_room_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='host',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='votes_to_skip',
            new_name='phd',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='guest_can_pause',
            new_name='remember_me',
        ),
    ]
