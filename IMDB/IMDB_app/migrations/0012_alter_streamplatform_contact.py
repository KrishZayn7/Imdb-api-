# Generated by Django 4.1 on 2022-08-31 10:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMDB_app', '0011_alter_streamplatform_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streamplatform',
            name='contact',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(message='Phone number must not excees 10 digits.', regex='^[0-9]{2}-[0-9]{10}$')]),
        ),
    ]
