# Generated by Django 2.0.6 on 2019-12-26 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CitiTechApp', '0005_remove_event_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='userchoices',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
