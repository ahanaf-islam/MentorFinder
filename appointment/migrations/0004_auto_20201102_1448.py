# Generated by Django 2.2.13 on 2020-11-02 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_auto_20201102_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateTimeField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
