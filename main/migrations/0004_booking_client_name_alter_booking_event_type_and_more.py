# Generated by Django 5.1.3 on 2025-01-23 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_number_of_people_booking_num_people'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='client_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='event_type',
            field=models.CharField(choices=[('Wedding', 'Wedding'), ('Graduation', 'Graduation'), ('Private', 'Private '), ('Anniversary', 'Anniversary'), ('Unspecified', 'Unspecified')], default='Wedding Event', max_length=50),
        ),
        migrations.AlterField(
            model_name='booking',
            name='num_people',
            field=models.CharField(choices=[('50-100', '50-100'), ('100-200', '200-500'), ('500-1000', '500-1000'), ('1000+', '1000+')], default='50-100 People', max_length=50),
        ),
    ]
