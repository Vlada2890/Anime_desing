# Generated by Django 4.2.3 on 2023-07-04 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_location_customuser_roach_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='roach',
        ),
    ]