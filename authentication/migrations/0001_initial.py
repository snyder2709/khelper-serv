# Generated by Django 4.2.6 on 2023-10-31 10:43

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=20, unique=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=70, unique=True)),
                ('password', models.CharField(max_length=12)),
                ('data_created', models.DateField(auto_now_add=True)),
                ('roles', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
