# Generated by Django 4.2.6 on 2023-10-31 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='roles',
        ),
    ]
