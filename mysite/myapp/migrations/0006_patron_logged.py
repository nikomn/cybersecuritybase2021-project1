# Generated by Django 3.1.7 on 2021-04-23 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20210423_0646'),
    ]

    operations = [
        migrations.AddField(
            model_name='patron',
            name='logged',
            field=models.TextField(default='False'),
        ),
    ]
