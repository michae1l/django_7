# Generated by Django 4.0.5 on 2022-06-14 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_stage7', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel_recorde',
            name='amount_paid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='hotel_recorde',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='hotel_recorde',
            name='number_of_night',
            field=models.IntegerField(max_length=50),
        ),
        migrations.AlterField(
            model_name='hotel_recorde',
            name='room_number',
            field=models.IntegerField(max_length=50),
        ),
        migrations.AlterField(
            model_name='hotel_recorde',
            name='start_date',
            field=models.DateField(),
        ),
    ]
