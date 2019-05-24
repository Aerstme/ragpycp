# Generated by Django 2.2.1 on 2019-05-19 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190519_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='state',
            field=models.PositiveIntegerField(choices=[(0, 'Active'), (1, 'Banned')], default=0, verbose_name='RO State'),
        ),
    ]
