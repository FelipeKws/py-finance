# Generated by Django 4.0.5 on 2022-06-29 01:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_alter_spent_method_fk'),
    ]

    operations = [
        migrations.AddField(
            model_name='incoming',
            name='dateEarn',
            field=models.DateField(default=datetime.datetime(2022, 6, 29, 1, 59, 40, 52210, tzinfo=utc), verbose_name='Date of earn'),
        ),
    ]
