# Generated by Django 5.0.7 on 2024-08-10 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0002_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
