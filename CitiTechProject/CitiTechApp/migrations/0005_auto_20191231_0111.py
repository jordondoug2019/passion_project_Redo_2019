# Generated by Django 2.0.6 on 2019-12-31 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CitiTechApp', '0004_auto_20191230_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userchoices',
            name='password',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='userchoices',
            name='username',
            field=models.CharField(default=' ', max_length=20),
        ),
    ]
