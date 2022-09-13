# Generated by Django 4.1 on 2022-08-30 06:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMDB_app', '0005_streamplatform_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streamplatform',
            name='contact',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(message='Phone number must be 10 digits long', regex='\\\\+?[1,9][0,9]{10}$')]),
        ),
    ]
