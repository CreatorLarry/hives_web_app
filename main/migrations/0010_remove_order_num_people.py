# Generated by Django 5.1.3 on 2025-01-24 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_orderableitem_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='num_people',
        ),
    ]
