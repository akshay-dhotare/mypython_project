# Generated by Django 4.1.5 on 2023-01-24 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=100)),
                ('days', models.IntegerField()),
                ('adhar_no', models.CharField(max_length=100)),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(max_length=100)),
                ('no_of_persons', models.IntegerField()),
                ('room_type', models.CharField(choices=[('sr', 'standard'), ('dr', 'deluxe'), ('sdr', 'superdeluxe')], max_length=3)),
            ],
        ),
    ]