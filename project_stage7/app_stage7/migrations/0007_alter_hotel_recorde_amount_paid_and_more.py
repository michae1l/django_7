# Generated by Django 4.0.5 on 2022-06-16 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_stage7', '0006_alter_hotel_recorde_amount_paid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel_recorde',
            name='amount_paid',
            field=models.CharField(max_length=510),
        ),
        migrations.AlterField(
            model_name='hotel_recorde',
            name='end_date',
            field=models.CharField(max_length=510),
        ),
        migrations.AlterField(
            model_name='hotel_recorde',
            name='number_of_night',
            field=models.CharField(max_length=510),
        ),
        migrations.AlterField(
            model_name='hotel_recorde',
            name='room_number',
            field=models.CharField(max_length=510),
        ),
        migrations.AlterField(
            model_name='hotel_recorde',
            name='start_date',
            field=models.CharField(max_length=510),
        ),
    ]
