# Generated by Django 5.1.3 on 2025-01-24 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_booking_client_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderableItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(max_length=100)),
                ('town', models.CharField(max_length=100)),
                ('place_name', models.CharField(max_length=200)),
                ('specifications', models.TextField(default='No specifications provided')),
                ('num_people', models.CharField(choices=[('50-100', '50-100'), ('100-200', '200-500'), ('500-1000', '500-1000'), ('1000+', '1000+')], default='50-100 People', max_length=50)),
                ('additional_notes', models.TextField(blank=True, null=True)),
                ('contact_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('client_name', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('items', models.ManyToManyField(related_name='orders', to='main.orderableitem')),
            ],
        ),
    ]
