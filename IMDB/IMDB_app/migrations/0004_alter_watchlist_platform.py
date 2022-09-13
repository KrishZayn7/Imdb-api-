# Generated by Django 4.1 on 2022-08-30 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IMDB_app', '0003_watchlist_platform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='IMDB_app.streamplatform'),
        ),
    ]