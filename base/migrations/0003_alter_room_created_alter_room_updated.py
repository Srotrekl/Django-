# Generated by Django 4.1.1 on 2022-09-11 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_room_participants_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
