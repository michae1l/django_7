# Generated by Django 4.0.5 on 2022-06-14 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_stage7', '0003_alter_hotel_recorde_number_of_night'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel_recorde',
            name='room_number',
            field=models.IntegerField(),
        ),
    ]