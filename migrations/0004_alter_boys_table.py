# Generated by Django 4.1.5 on 2023-03-14 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resortapp', '0003_rename_student_boys_alter_boys_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='boys',
            table='boy',
        ),
    ]
