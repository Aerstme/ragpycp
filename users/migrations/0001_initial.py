# Generated by Django 2.2.1 on 2019-05-18 21:19

import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.CharField(max_length=23, unique=True)),
                ('user_pass', models.CharField(max_length=32)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('email', models.CharField(max_length=39, unique=True)),
                ('group_id', models.IntegerField(default=0)),
                ('state', models.PositiveIntegerField(default=0)),
                ('unban_time', models.PositiveIntegerField(null=True)),
                ('expiration_time', models.PositiveIntegerField(null=True)),
                ('logincount', models.PositiveIntegerField(default=0)),
                ('lastlogin', models.DateTimeField(blank=True, null=True)),
                ('last_ip', models.CharField(max_length=100, null=True)),
                ('birthdate', models.DateField(null=True)),
                ('character_slots', models.PositiveIntegerField(null=True)),
                ('pincode', models.CharField(max_length=4, null=True)),
                ('pincode_change', models.PositiveIntegerField(default=0)),
                ('vip_time', models.PositiveIntegerField(null=True)),
                ('old_group', models.IntegerField(null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'login',
                'managed': True,
            },
            managers=[
                ('objects', users.models.CustomUserManager()),
            ],
        ),
    ]
