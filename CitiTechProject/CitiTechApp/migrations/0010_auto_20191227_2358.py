# Generated by Django 2.0.6 on 2019-12-27 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CitiTechApp', '0009_auto_20191227_2325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userchoices',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='userchoices',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='userchoices',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='userchoices',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='userchoices',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='userchoices',
            name='user_permissions',
        ),
    ]