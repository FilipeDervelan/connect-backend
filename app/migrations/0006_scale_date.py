# Generated by Django 5.0.4 on 2024-05-02 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_function_ministry'),
    ]

    operations = [
        migrations.AddField(
            model_name='scale',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]