from django.db import models


# Create your models here.
class Booking(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    No_of_guests = models.PositiveSmallIntegerField()
    BookingDate = models.DateTimeField()


class Menu(models.Model):
    ID = models.SmallAutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.SmallIntegerField()
