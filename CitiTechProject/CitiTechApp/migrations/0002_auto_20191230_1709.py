# Generated by Django 2.0.6 on 2019-12-30 17:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('CitiTechApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userchoices',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]