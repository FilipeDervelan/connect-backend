# Generated by Django 5.0.4 on 2024-11-23 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_customuser_created_at_customuser_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='ministry',
            name='owner_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
