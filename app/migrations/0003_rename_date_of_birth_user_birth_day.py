# Generated by Django 5.0.4 on 2024-04-30 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_ministry_participant_function_ministry_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='date_of_birth',
            new_name='birth_day',
        ),
    ]
