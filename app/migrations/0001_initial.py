# Generated by Django 5.0.4 on 2024-11-23 13:59

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ministry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Ministries',
                'db_table': 'ministry',
            },
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Singers',
                'db_table': 'singer',
            },
        ),
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('ministry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ministry')),
            ],
            options={
                'verbose_name_plural': 'Functions',
                'db_table': 'function',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('birth_day', models.DateField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('function', models.ManyToManyField(blank=True, to='app.function')),
                ('ministry', models.ManyToManyField(blank=True, to='app.ministry')),
            ],
            options={
                'verbose_name_plural': 'Custom Users',
                'db_table': 'custom_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('singer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.singer')),
            ],
            options={
                'verbose_name_plural': 'Songs',
                'db_table': 'song',
            },
        ),
        migrations.CreateModel(
            name='Scale',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('function', models.ManyToManyField(blank=True, null=True, to='app.function')),
                ('ministry', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.ministry')),
                ('participant', models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
                ('song', models.ManyToManyField(blank=True, null=True, to='app.song')),
            ],
            options={
                'verbose_name_plural': 'Scales',
                'db_table': 'scale',
            },
        ),
        migrations.CreateModel(
            name='Unavailability',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Unavailabilities',
                'db_table': 'unavailability',
            },
        ),
    ]
