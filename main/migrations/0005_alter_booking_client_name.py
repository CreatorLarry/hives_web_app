# Generated by Django 5.1.3 on 2025-01-23 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_booking_client_name_alter_booking_event_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='client_name',
            field=models.CharField(max_length=255),
        ),
    ]
