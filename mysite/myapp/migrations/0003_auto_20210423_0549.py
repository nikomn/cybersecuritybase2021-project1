# Generated by Django 3.1.7 on 2021-04-23 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210422_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.TextField()),
                ('information', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(default='No address', max_length=140),
        ),
        migrations.AddField(
            model_name='user',
            name='firts_name',
            field=models.TextField(default='', max_length=140),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.TextField(default='', max_length=140),
        ),
        migrations.AddField(
            model_name='user',
            name='ssn',
            field=models.TextField(default='', max_length=140),
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user'),
        ),
    ]