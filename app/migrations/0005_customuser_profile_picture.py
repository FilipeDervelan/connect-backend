# Generated by Django 5.0.4 on 2025-03-05 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_scale_function'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
    ]
