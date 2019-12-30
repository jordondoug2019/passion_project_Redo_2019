# Generated by Django 2.0.6 on 2019-12-30 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CitiTechApp', '0003_auto_20191230_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userchoices',
            name='id',
        ),
        migrations.AddField(
            model_name='userchoices',
            name='userOnetoOne',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
