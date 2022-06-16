from tokenize import Name
from django.db import models


# Create your models here.

class hotel_recorde(models.Model):
    room_number = models.CharField(max_length=510)
    amount_paid = models.CharField(max_length=510)
    occupant_name = models.CharField(max_length=510)
    occupant_email = models.EmailField()
    occupant_occupation = models.CharField(max_length=50)
    number_of_night = models.CharField(max_length=510)
    start_date = models.CharField(max_length=510)
    end_date = models.CharField(max_length=510)






